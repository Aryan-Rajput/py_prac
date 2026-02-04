-- =========================
-- SCHEMA: ELECTRICAL MADNESS
-- =========================

-- BEGIN
--   EXECUTE IMMEDIATE 'DROP TABLE reading' WHERE EXISTS (SELECT 1 FROM user_tables WHERE table_name = 'READING');
-- EXCEPTION WHEN OTHERS THEN NULL;
-- END;
-- /
-- BEGIN
--   EXECUTE IMMEDIATE 'DROP TABLE switchstate' WHERE EXISTS (SELECT 1 FROM user_tables WHERE table_name = 'SWITCHSTATE');
-- EXCEPTION WHEN OTHERS THEN NULL;
-- END;
-- /
-- BEGIN
--   EXECUTE IMMEDIATE 'DROP TABLE wire' WHERE EXISTS (SELECT 1 FROM user_tables WHERE table_name = 'WIRE');
-- EXCEPTION WHEN OTHERS THEN NULL;
-- END;
-- /
-- BEGIN
--   EXECUTE IMMEDIATE 'DROP TABLE node' WHERE EXISTS (SELECT 1 FROM user_tables WHERE table_name = 'NODE');
-- EXCEPTION WHEN OTHERS THEN NULL;
-- END;
-- /
 
DROP TABLE IF EXISTS node; -- AS
CREATE TABLE node (
  nodeid      INT PRIMARY KEY,
  nodename    TEXT NOT NULL,
  zone         TEXT NOT NULL
);
 
DROP TABLE IF EXISTS wire;
CREATE TABLE wire (
  wireid      INT PRIMARY KEY,
  fromnode    INT NOT NULL REFERENCES node(nodeid),
  tonode      INT NOT NULL REFERENCES node(nodeid),
  resistanceohm NUMERIC(10,3) NOT NULL,
  islive      BOOLEAN NOT NULL DEFAULT TRUE
);

drop table if exists switchstate;
CREATE TABLE switchstate (
  switchid    INT PRIMARY KEY,
  nodeid      INT NOT NULL REFERENCES node(nodeid),
  state        TEXT NOT NULL CHECK (state IN ('ON','OFF','FLAPPING')),
  updatedat   TIMESTAMP NOT NULL
);
 
DROP TABLE IF EXISTS reading;
CREATE TABLE reading (
  readingid   INT PRIMARY KEY,
  nodeid      INT NOT NULL REFERENCES node(nodeid),
  amps         NUMERIC(10,3),
  volts        NUMERIC(10,3),
  readingts   TIMESTAMP NOT NULL
);

-- ======================
-- SCHEMA: FROG MAZE PUZZLE
-- ======================

-- BEGIN
--   EXECUTE IMMEDIATE 'DROP TABLE jump' WHERE EXISTS (SELECT 1 FROM user_tables WHERE table_name = 'JUMP');
-- EXCEPTION WHEN OTHERS THEN NULL;
-- END;
-- /
-- BEGIN
--   EXECUTE IMMEDIATE 'DROP TABLE welllink' WHERE EXISTS (SELECT 1 FROM user_tables WHERE table_name = 'WELLINK');
-- EXCEPTION WHEN OTHERS THEN NULL;
-- END;
-- /
-- BEGIN
--   EXECUTE IMMEDIATE 'DROP TABLE frog' WHERE EXISTS (SELECT 1 FROM user_tables WHERE table_name = 'FROG');
-- EXCEPTION WHEN OTHERS THEN NULL;
-- END;
-- /
-- BEGIN
--   EXECUTE IMMEDIATE 'DROP TABLE well' WHERE EXISTS (SELECT 1 FROM user_tables WHERE table_name = 'WELL');
-- EXCEPTION WHEN OTHERS THEN NULL;
-- END;
-- /

DROP TABLE IF EXISTS well;
CREATE TABLE well (
  wellid    INT PRIMARY KEY,
  wellname  TEXT NOT NULL,
  depthm    INT NOT NULL,
  hazard     INT NOT NULL CHECK (hazard BETWEEN 0 AND 10)
);
 
DROP TABLE IF EXISTS frog;
CREATE TABLE frog (
  frogid       INT PRIMARY KEY,
  frogname     TEXT NOT NULL,
  chargelevel  INT NOT NULL,        -- like stamina/energy
  homewellid  INT NOT NULL REFERENCES well(wellid)
);
 
-- Directed graph of allowed jumps (maze)
DROP TABLE IF EXISTS welllink;
CREATE TABLE welllink (
  fromwell INT NOT NULL REFERENCES well(wellid),
  towell   INT NOT NULL REFERENCES well(wellid),
  voltscost INT NOT NULL,
  PRIMARY KEY (fromwell, towell)
);
 
DROP TABLE IF EXISTS jump;
CREATE TABLE jump (
  jumpid   INT PRIMARY KEY,
  frogid   INT NOT NULL REFERENCES frog(frogid),
  fromwell INT NOT NULL REFERENCES well(wellid),
  towell   INT NOT NULL REFERENCES well(wellid),
  jumpts   TIMESTAMP NOT NULL,
  voltsspent INT,
  -- some rows intentionally NULL voltsspent to test COALESCE
  CHECK (fromwell <> towell)
);
 

-- ======================
-- SEED DATA
-- ======================
INSERT INTO node VALUES
(1,'N1Coil','ZA'),
(2,'N2Cap','ZA'),
(3,'N3Ground','ZA'),
(4,'N4Surge','ZB'),
(5,'N5Fuse','ZB'),
(6,'N6Lab','ZC');
 
INSERT INTO wire VALUES
(101,1,2,0.200,TRUE),
(102,2,3,0.050,TRUE),
(103,2,4,0.900,TRUE),
(104,4,5,0.010,TRUE),
(105,5,6,0.300,TRUE),
(106,6,2,0.150,TRUE),        -- creates a cycle 2->4->5->6->2
(107,1,3,5.000,FALSE);       -- dead wire

-- Fromnode does NOT exist (999)
INSERT INTO wire VALUES
(108, 999, 2, 0.123, TRUE);

-- Tonode does NOT exist (888)
INSERT INTO wire VALUES
(109, 3, 888, 0.456, TRUE);

-- BOTH fromnode AND tonode missing
INSERT INTO wire VALUES
(110, 777, 666, 0.789, TRUE);

-- Self-loop test (valid but weird)
INSERT INTO wire VALUES
(111, 4, 4, 0.050, TRUE);

-- Cross-zone valid wire using your new nodes
INSERT INTO wire VALUES
(112, 1, 20, 1.000, TRUE);

-- Wire to deprecated node
INSERT INTO wire VALUES
(113, 15, 5, 0.050, TRUE);



-- More switch events per node to exercise time-based joins and ROW_NUMBER
INSERT INTO switchstate VALUES
(204, 2, 'OFF',     '2026-01-20 10:07:00'),
(205, 2, 'OFF',     '2026-01-21 08:59:00'),
(206, 2, 'ON',      '2026-01-21 09:06:00'),
(207, 4, 'OFF',     '2026-01-20 10:07:00'),
(208, 4, 'FLAPPING','2026-01-21 09:04:00'),
(209, 6, 'OFF',     '2026-01-21 10:00:00'),
(210, 1, 'ON',      '2026-01-20 09:59:00'); -- Node 1 had no readings before; good for "no match" edge case

 
--  -------------------------------------------------------------------

-- Node 2 readings before/after various switch updates
INSERT INTO reading VALUES
(307, 2, 1.180, 110.0, '2026-01-20 09:58:00'),
(308, 2, 1.220, 110.0, '2026-01-20 09:59:30'),
(309, 2, 1.260, 110.0, '2026-01-20 10:03:00'),
(310, 2, NULL,  110.0, '2026-01-20 10:04:00'), -- NULL amps to test COALESCE
(311, 2, 1.255, 110.0, '2026-01-20 10:06:59'), -- immediately before switch 204
(312, 2, 1.270, 110.0, '2026-01-20 10:07:01'), -- just after switch 204 (should be excluded by <=)
(313, 2, 1.100, 110.0, '2026-01-21 08:58:30'), -- for switch 205
(314, 2, 1.300, 110.0, '2026-01-21 09:05:59'); -- for switch 206

-- Node 4 readings around flapping/off events
INSERT INTO reading VALUES
(315, 4,  9.700, 220.0, '2026-01-20 10:04:30'),
(316, 4, 10.600, 220.0, '2026-01-20 10:06:30'),
(317, 4, 10.700, 220.0, '2026-01-20 10:07:30'), -- after switch 207 (excluded by <=)
(318, 4,  8.900, 220.0, '2026-01-21 09:03:50'), -- just before 208
(319, 4,  9.000, 220.0, '2026-01-21 09:04:10'); -- just after 208 (excluded)

-- Node 6 varied readings
INSERT INTO reading VALUES
(320, 6,  0.095, 24.0,  '2026-01-21 09:59:30'),
(321, 6,  0.101, 24.0,  '2026-01-21 10:00:00'), -- exactly at switch 209 time (included)
(322, 6,  0.200, 24.0,  '2026-01-21 10:00:01'); -- just after (excluded)

-- Node 1 readings (appear *after* switch 210, so <= filter fails → good negative case)
INSERT INTO reading VALUES
(323, 1,  0.500, 110.0, '2026-01-20 10:00:01'),
(324, 1,  0.450, 110.0, '2026-01-20 10:05:00');

 
INSERT INTO well VALUES
(1,'W1Alpha', 12,2),
(2,'W2Beta',  30,7),
(3,'W3Gamma', 25,3),
(4,'W4Delta', 18,9),
(5,'W5Epsilon',40,1),
(6,'W6Zeta',  22,5);


-- new wells to test more complex paths
INSERT INTO well VALUES
(7,'W7Eta',   28,4),
(8,'W8Theta', 16,6);

 
INSERT INTO frog VALUES
(1,'FrogZap',  120,1),
(2,'FrogSpark', 60, 2),
(3,'FrogNull',  50, 3);


-- new frogs to test more complex paths
INSERT INTO frog VALUES
(4,'FrogBolt',  80, 4),
(5,'FrogEcho', 150, 5);

 
INSERT INTO welllink VALUES
(1,2,20),(2,3,15),(3,4,40),(4,5,10),(5,6,15),(6,1,25), -- cycle
(1,3,35),(2,5,50),(3,6,10),(2,4,5);  -- sneaky shortcuts


-- new welllinks to create more complex paths and cycles
INSERT INTO welllink VALUES
(5,7,  5),(7,8, 12),(8,2, 18),    -- connects back near the original cycle
(3,5, 20),    -- alternative route
(6,7, 10),    -- fork
(8,6,  8);    -- small cycle 6 -> 7 -> 8 -> 6 possible

 
INSERT INTO jump VALUES
(401,1,1,2,'2026-01-21 09:00:00',20),
(402,1,2,4,'2026-01-21 09:05:00',NULL), -- missing volts_spent
(403,1,4,5,'2026-01-21 09:10:00',10),
(404,2,2,3,'2026-01-21 09:00:00',15),
(405,2,3,6,'2026-01-21 09:10:00',10),
(406,3,3,6,'2026-01-21 09:00:00',NULL);


-- new jumps to test more complex paths and NULL voltsspent
INSERT INTO jump VALUES
(407,1,5,6,'2026-01-21 09:20:00', 15),
(408,1,6,1,'2026-01-21 09:30:00', NULL), -- NULL voltsspent to test COALESCE/SUM
(409,2,3,4,'2026-01-21 09:20:00', 40),
(410,2,4,5,'2026-01-21 09:25:00', 10),
(411,4,4,5,'2026-01-21 09:15:00', NULL),  -- FrogBolt unknown cost
(412,5,5,7,'2026-01-21 09:10:00',  5),
(413,5,7,8,'2026-01-21 09:12:00', 12),
(414,5,8,2,'2026-01-21 09:14:00', 18);
