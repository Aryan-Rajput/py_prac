
SELECT
  j.jumpid, j.frogid, j.fromwell, j.towell,
  wl.voltscost
FROM jump j
LEFT JOIN welllink wl
  ON j.fromwell = wl.fromwell
AND j.towell   = wl.towell
WHERE wl.voltscost IS NULL;
-- there are no null results, meaning all jumps have corresponding welllink entries.


select * from jump;
select * from welllink;