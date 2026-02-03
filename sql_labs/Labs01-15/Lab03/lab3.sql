SELECT
  COALESCE(j.fromwell, wl.fromwell) AS fromwell,
  COALESCE(j.towell,   wl.towell)   AS towell,
  j.jumpid,
  wl.voltscost
FROM jump j
FULL JOIN welllink wl
  ON j.fromwell = wl.fromwell
AND j.towell   = wl.towell;
 
-- this shows all welllink entries and any jump entries that do not have a corresponding welllink entry
-- i.e. welllinks that were not used for any jumps
