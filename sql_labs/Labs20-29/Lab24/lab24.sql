 
WITH nodefeatures AS (
  SELECT
    nodeid,
    -- amps,
    SUM(CASE WHEN amps IS NULL THEN 1 ELSE 0 END) AS nullamps,
    AVG(CASE WHEN amps IS NOT NULL THEN amps END) AS avgamps
  FROM reading
  GROUP BY nodeid
)
SELECT
  n.nodeid, n.nodename, n.zone,
  COALESCE(f.nullamps, 0) AS nullamps,
  f.avgamps
FROM node n
LEFT JOIN nodefeatures f ON f.nodeid = n.nodeid
ORDER BY n.nodeid;

select * from reading;