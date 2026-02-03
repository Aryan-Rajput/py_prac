
-- objective: combine jump records with well_link data to compare 
--            the volts used in actual jumps vs the expected volts for that route.

select
    j.jumpid,           -- unique identifier for each jump
    j.frogid,           -- id of the frog that made the jump
    j.fromwell,         -- starting well location
    j.towell,           -- destination well location
    j.voltsspent,       -- actual energy used by the frog
    wl.voltscost as expectedcost  -- expected energy cost for this route
from jump j
join welllink wl
    on j.fromwell = wl.fromwell
    and j.towell   = wl.towell;
-- this result shows:
-- - each jump record paired with its corresponding route cost
-- - jumpid: the specific jump event being analyzed
-- - frogid: which frog made this jump
-- - fromwell and towell: the route taken
-- - voltsspent vs expectedcost: comparison of actual vs expected energy
--   (helps identify inefficient jumps where voltsspent > expectedcost,
--    or anomalies where voltsspent < expectedcost)

select * from jump;
select * from welllink;