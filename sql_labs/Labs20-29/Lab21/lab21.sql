SELECT *
FROM (
  SELECT
    s.switchid, s.nodeid, s.updatedat, s.state,
    r.readingts, r.amps,
    ROW_NUMBER() OVER (
      PARTITION BY s.switchid
      ORDER BY r.readingts DESC
    ) AS rn
  FROM switchstate s
  JOIN reading r
    ON r.nodeid = s.nodeid
   AND r.readingts <= s.updatedat
) z
WHERE rn = 1
ORDER BY nodeid, updatedat;
 
