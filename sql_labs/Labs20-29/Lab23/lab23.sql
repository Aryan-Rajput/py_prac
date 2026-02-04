
SELECT
  w.wireid,
  w.fromnode, n1.nodename AS fromname,
  w.tonode,   n2.nodename AS toname,
  CASE
    WHEN n1.nodeid IS NULL THEN 'MISSINGFROMNODE'
    WHEN n2.nodeid IS NULL THEN 'MISSINGTONODE'
    ELSE 'OK'
  END AS status
FROM wire w
LEFT JOIN node n1 ON n1.nodeid = w.fromnode
LEFT JOIN node n2 ON n2.nodeid = w.tonode
ORDER BY w.wireid;


SELECT * FROM WIRE;
SELECT * FROM NODE;