SELECT
    J.*,
    F.CHARGELEVEL
    -- Calculate the energy left after each jump by subtracting the cumulative
    -- volts spent from the frog's initial charge level
    - SUM(COALESCE(J.VOLTSSPENT, 0)) OVER (
        PARTITION BY J.FROGID
        ORDER BY J.JUMPTS
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS ENERGYLEFT
FROM JUMP J
JOIN FROG F ON F.FROGID = J.FROGID
ORDER BY J.FROGID, J.JUMPTS;
