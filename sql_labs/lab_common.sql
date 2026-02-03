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
 
CREATE TABLE node (
  nodeid      INT PRIMARY KEY,
  nodename    TEXT NOT NULL,
  zone         TEXT NOT NULL
);
 
CREATE TABLE wire (
  wireid      INT PRIMARY KEY,
  fromnode    INT NOT NULL REFERENCES node(nodeid),
  tonode      INT NOT NULL REFERENCES node(nodeid),
  resistanceohm NUMERIC(10,3) NOT NULL,
  islive      BOOLEAN NOT NULL DEFAULT TRUE
);
 
CREATE TABLE switchstate (
  switchid    INT PRIMARY KEY,
  nodeid      INT NOT NULL REFERENCES node(nodeid),
  state        TEXT NOT NULL CHECK (state IN ('ON','OFF','FLAPPING')),
  updatedat   TIMESTAMP NOT NULL
);
 
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
 
CREATE TABLE well (
  wellid    INT PRIMARY KEY,
  wellname  TEXT NOT NULL,
  depthm    INT NOT NULL,
  hazard     INT NOT NULL CHECK (hazard BETWEEN 0 AND 10)
);
 
CREATE TABLE frog (
  frogid       INT PRIMARY KEY,
  frogname     TEXT NOT NULL,
  chargelevel  INT NOT NULL,        -- like stamina/energy
  homewellid  INT NOT NULL REFERENCES well(wellid)
);
 
-- Directed graph of allowed jumps (maze)
CREATE TABLE welllink (
  fromwell INT NOT NULL REFERENCES well(wellid),
  towell   INT NOT NULL REFERENCES well(wellid),
  voltscost INT NOT NULL,
  PRIMARY KEY (fromwell, towell)
);
 
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
(1,'N1Coil','ZA'),(2,'N2Cap','ZA'),(3,'N3Ground','ZA'),
(4,'N4Surge','ZB'),(5,'N5Fuse','ZB'),(6,'N6Lab','ZC');
 
INSERT INTO wire VALUES
(101,1,2,0.200,TRUE),
(102,2,3,0.050,TRUE),
(103,2,4,0.900,TRUE),
(104,4,5,0.010,TRUE),
(105,5,6,0.300,TRUE),
(106,6,2,0.150,TRUE),        -- creates a cycle 2->4->5->6->2
(107,1,3,5.000,FALSE);       -- dead wire
 
INSERT INTO switchstate VALUES
(201,2,'ON',      '2026-01-20 10:00:00'),
(202,4,'FLAPPING','2026-01-20 10:05:00'),
(203,6,'OFF',     '2026-01-20 10:10:00');
 
INSERT INTO reading VALUES
(301,2, 1.200, 110.0,'2026-01-20 10:00:00'),
(302,2, 1.250, 110.0,'2026-01-20 10:01:00'),
(303,2, NULL,  110.0,'2026-01-20 10:02:00'), -- NULL amps
(304,4, 9.900, 220.0,'2026-01-20 10:05:00'),
(305,4, 10.5,  220.0,'2026-01-20 10:06:00'),
(306,6, 0.100, 24.0, '2026-01-20 10:10:00');
 
INSERT INTO well VALUES
(1,'W1Alpha', 12,2),
(2,'W2Beta',  30,7),
(3,'W3Gamma', 25,3),
(4,'W4Delta', 18,9),
(5,'W5Epsilon',40,1),
(6,'W6Zeta',  22,5);
 
INSERT INTO frog VALUES
(1,'FrogZap',  120,1),
(2,'FrogSpark', 60, 2),
(3,'FrogNull',  50, 3);
 
INSERT INTO welllink VALUES
(1,2,20),(2,3,15),(3,4,40),(4,5,10),(5,6,15),(6,1,25), -- cycle
(1,3,35),(2,5,50),(3,6,10),(2,4,5);  -- sneaky shortcuts
 
INSERT INTO jump VALUES
(401,1,1,2,'2026-01-21 09:00:00',20),
(402,1,2,4,'2026-01-21 09:05:00',NULL), -- missing volts_spent
(403,1,4,5,'2026-01-21 09:10:00',10),
(404,2,2,3,'2026-01-21 09:00:00',15),
(405,2,3,6,'2026-01-21 09:10:00',10),
(406,3,3,6,'2026-01-21 09:00:00',NULL);