-- This query calculates the average current (AMPS) readings for each NODEID from the READING table.
-- It uses a Common Table Expression (CTE) named STATS to compute the average AMPS for each NODEID,
-- excluding any NULL values. The main query then selects the NODEID, reading timestamp (READINGTS),
-- individual AMPS readings, and the calculated average AMPS from the READING table.
-- Additionally, it flags readings as 'SURGE' if the AMPS value exceeds three times the average AMPS,
-- otherwise it flags them as 'OK'. The results are ordered by NODEID and reading timestamp.

WITH STATS AS (
    SELECT
        NODEID,
        AVG(AMPS) AS AVGAMPS
    FROM READING
    WHERE AMPS IS NOT NULL
    GROUP BY NODEID
)
SELECT
    R.NODEID, R.READINGTS, R.AMPS, ROUND(S.AVGAMPS, 4) AS AVGAMPS,
    CASE WHEN R.AMPS > 3 * S.AVGAMPS THEN 'SURGE' ELSE 'OK' END AS FLAG
FROM READING R
JOIN STATS S ON S.NODEID = R.NODEID
WHERE R.AMPS IS NOT NULL
ORDER BY R.NODEID, R.READINGTS;

SELECT * FROM READING ORDER BY NODEID, READINGTS;