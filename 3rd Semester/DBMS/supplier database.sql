create database IF NOT exists supplier_database;
use supplier_database;

create table SUPPLIERS(sid integer(5) primary key, sname varchar(20), city
varchar(20));
create table PARTS(pid integer(5) primary key, pname varchar(20), color varchar(10));

create table CATALOG(sid integer(5), pid integer(5), foreign key(sid)
references SUPPLIERS(sid), foreign key(pid) references PARTS(pid), cost
float(6), primary key(sid, pid));

insert into suppliers values(10001, ' Acme Widget','Bangalore');
insert into suppliers values(10002, ' Johns','Kolkata');
insert into suppliers values(10003, ' Vimal','Mumbai');
insert into suppliers values(10004, ' Reliance','Delhi');
insert into suppliers values(10005, ' Mahindra','Mumbai');

insert into PARTS values(20001, 'Book','Red');
insert into PARTS values(20002, 'Pen','Red');
insert into PARTS values(20003, 'Pencil','Green');
insert into PARTS values(20004, 'Mobile','Green');
insert into PARTS values(20005, 'Charger','Black');

insert into CATALOG values(10001, 20001,10);
insert into CATALOG values(10001, 20002,10);
insert into CATALOG values(10001, 20003,30);
insert into CATALOG values(10001, 20004,10);
insert into CATALOG values(10001, 20005,10);
insert into CATALOG values(10002, 20001,10);
insert into CATALOG values(10002, 20002,20);
insert into CATALOG values(10003, 20003,30);
insert into CATALOG values(10004, 20003,40);

SELECT DISTINCT P.pname
FROM Parts P, Catalog C
WHERE P.pid = C.pid;

SELECT S.sname
FROM Suppliers S
WHERE
(( SELECT count(P.pid)
FROM Parts P ) =
( SELECT count(C.pid)
FROM Catalog C
WHERE C.sid = S.sid ));

SELECT S.sname
FROM Suppliers S
WHERE
(( SELECT count(P.pid)
FROM Parts P where color='Red' ) =
( SELECT count(C.pid)
FROM Catalog C, Parts P
WHERE C.sid = S.sid AND
C.pid = P.pid AND P.color = 'Red'));

SELECT P.pname
FROM Parts P, Catalog C, Suppliers S
WHERE P.pid = C.pid
  AND C.sid = S.sid
  AND S.sname = 'Acme Widget'
  AND NOT EXISTS (
        SELECT *
        FROM Catalog C1, Suppliers S1
        WHERE P.pid = C1.pid
          AND C1.sid = S1.sid
          AND S1.sname <> 'Acme Widget');
  
  SELECT DISTINCT C.sid FROM Catalog C
 WHERE C.cost > ( SELECT AVG (C1.cost)
 FROM Catalog C1
 WHERE C1.pid = C.pid );
 
SELECT P.pid, S.sname
FROM Parts P, Suppliers S, Catalog C
WHERE C.pid = P.pid
AND C.sid = S.sid
AND C.cost = (SELECT MAX(C1.cost)
FROM Catalog C1
WHERE C1.pid = P.pid);


SELECT p.pid, p.pname, c.sid, s.sname, c.cost
FROM CATALOG c
JOIN PARTS p ON c.pid = p.pid
JOIN SUPPLIERS s ON c.sid = s.sid
WHERE c.cost = (SELECT MAX(cost) FROM CATALOG);


SELECT s.sid, s.sname
FROM SUPPLIERS s
WHERE NOT EXISTS (
    SELECT 1
    FROM CATALOG c
    JOIN PARTS p ON c.pid = p.pid
    WHERE c.sid = s.sid AND p.color = 'Red'
);


SELECT s.sid, s.sname,
       IFNULL(SUM(c.cost), 0) AS total_value
FROM SUPPLIERS s
LEFT JOIN CATALOG c ON s.sid = c.sid
GROUP BY s.sid, s.sname;


SELECT s.sid, s.sname
FROM SUPPLIERS s
JOIN CATALOG c ON s.sid = c.sid
WHERE c.cost < 20
GROUP BY s.sid, s.sname
HAVING COUNT(*) >= 2;

SELECT c.sid, s.sname, c.pid, p.pname, c.cost
FROM CATALOG c
JOIN SUPPLIERS s ON s.sid = c.sid
JOIN PARTS p ON p.pid = c.pid
WHERE c.cost = (
    SELECT MIN(c2.cost)
    FROM CATALOG c2
    WHERE c2.pid = c.pid
);



CREATE VIEW SupplierPartCount AS
SELECT s.sid, s.sname,
       COUNT(c.pid) AS num_parts
FROM SUPPLIERS s
LEFT JOIN CATALOG c ON s.sid = c.sid
GROUP BY s.sid, s.sname;
 select * from SupplierPartCount;

CREATE VIEW MostExpensiveSupplier AS
SELECT c.sid, s.sname, c.pid, p.pname, c.cost
FROM CATALOG c
JOIN SUPPLIERS s ON c.sid = s.sid
JOIN PARTS p ON c.pid = p.pid
WHERE c.cost = (
    SELECT MAX(c2.cost)
    FROM CATALOG c2
    WHERE c2.pid = c.pid
);
 select * from MostExpensiveSupplier;


DELIMITER $$
CREATE TRIGGER cost_check
BEFORE INSERT ON CATALOG
FOR EACH ROW
BEGIN
    IF NEW.cost < 1 THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Cost cannot be below 1';
    END IF;
END$$
DELIMITER ;


DELIMITER $$
CREATE TRIGGER default_cost
BEFORE INSERT ON CATALOG
FOR EACH ROW
BEGIN
    IF NEW.cost IS NULL THEN
        SET NEW.cost = 50;
    END IF;
END$$
DELIMITER ;





select * from SUPPLIERS;
select * from PARTS;
select * from CATALOG;
commit;
