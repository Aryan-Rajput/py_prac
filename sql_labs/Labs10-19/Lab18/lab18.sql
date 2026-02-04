 
-- This can return ZERO rows if subquery contains NULL
SELECT *
FROM node
WHERE nodeid NOT IN (SELECT nodeid FROM reading);
 
-- Safer: NOT EXISTS
SELECT n.*
FROM node n
WHERE NOT EXISTS (
  SELECT 1
  FROM reading r
  WHERE r.nodeid = n.nodeid
);
 
SELECT * FROM NODE;
SELECT * FROM READING;