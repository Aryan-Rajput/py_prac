SELECT
  NODEID, READINGTS, AMPS,
  AVG(AMPS) OVER (
    PARTITION BY NODEID
    ORDER BY READINGTS
    -- This window frame clause defines the range of rows to be included in the window function calculation
    -- ROWS BETWEEN 2 PRECEDING AND CURRENT ROW means:
    --   - Start from 2 rows before the current row
    --   - End at the current row
    -- This creates a sliding window of up to 3 rows (2 preceding + current)
   ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
  ) AS AVG3LASTROWS
FROM READING
ORDER BY NODEID, READINGTS;

