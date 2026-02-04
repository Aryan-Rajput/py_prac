 
SELECT *
FROM (
  SELECT
    s.*,
    ROW_NUMBER() OVER (PARTITION BY nodeid ORDER BY updatedat DESC) AS rn
  FROM switchstate s
) x
WHERE rn = 1;
 
