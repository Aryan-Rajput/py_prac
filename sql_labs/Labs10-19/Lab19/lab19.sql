SELECT
  j.jumpid, j.frogid, j.fromwell, j.towell,
  COALESCE(j.voltsspent, -999) AS spent,
  wl.voltscost AS expected,
  CASE
    WHEN j.voltsspent IS NULL THEN 'MISSINGSPENT'
    WHEN j.voltsspent <> wl.voltscost THEN 'MISMATCH'
    ELSE 'OK'
  END AS status
FROM jump j
LEFT JOIN welllink wl
  ON wl.fromwell = j.fromwell AND wl.towell = j.towell
ORDER BY j.jumpid;


SELECT * FROM WELLlINK;
SELECT * FROM JUMP;