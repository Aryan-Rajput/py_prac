WITH LATEST AS (
    SELECT
        NODEID,
        MAX(READINGTS) AS MAXTS
    FROM READING
    GROUP BY NODEID
)
SELECT
    N.NODEID,
    N.NODENAME,
    R.READINGTS,
    COALESCE(R.AMPS, 0) AS AMPSSAFE
FROM NODE N
LEFT JOIN LATEST L ON L.NODEID = N.NODEID
LEFT JOIN READING R
    ON R.NODEID = L.NODEID AND R.READINGTS = L.MAXTS
ORDER BY N.NODEID;

-- this query retrieves the latest reading for each node ensuring that 
-- if there is no reading, the amps value defaults to 0

