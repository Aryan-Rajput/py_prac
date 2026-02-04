-- PARTITION BY frogid → do this separately for each frog.
-- ORDER BY jumpts → within each frog, sort jumps by time.
-- LAG(jumpts) → peek at the previous jump time for the current row.

-- For the first jump of a frog, prevts will be NULL (there’s no previous jump).
WITH x AS (
  SELECT
    frogid, jumpts,
    LAG(jumpts) OVER (PARTITION BY frogid ORDER BY jumpts) AS prevts
  FROM jump
),
-- If prevts IS NULL → first jump for the frog → new session (newsess = 1).
-- Otherwise, compute the time gap:
-- EXTRACT(EPOCH FROM (jumpts - prevts)) / 60 = gap in minutes (PostgreSQL style).

-- If gap > 7 minutes → new session.
-- Else → same session (newsess = 0).
y AS (
  SELECT *,
    CASE
      WHEN prevts IS NULL THEN 1
      WHEN EXTRACT(EPOCH FROM (jumpts - prevts)) / 60 > 7 THEN 1
      ELSE 0
    END AS newsess
  FROM x
)
-- We do a running sum of newsess per frog, in time order.
-- Every time newsess = 1, the running sum increases → session ID increases.
-- So sessions become: 1, 1, 1… then when a big gap occurs, it becomes 2, and so on.
SELECT
  frogid, jumpts, prevts,
  SUM(newsess) OVER (PARTITION BY frogid ORDER BY jumpts) AS sessionid
FROM y
ORDER BY frogid, jumpts;
 
