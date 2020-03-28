.read lab12.sql

CREATE TABLE sp19favpets AS
  SELECT pet, COUNT(*) as total FROM students GROUP BY pet ORDER BY total DESC LIMIT 10;


CREATE TABLE sp19dog AS
  SELECT pet, COUNT(*) FROM students WHERE pet = "dog";

CREATE TABLE sp19alldogs AS
  SELECT pet, COUNT(*) FROM students WHERE pet LIKE '%dog%';


CREATE TABLE obedienceimages AS
  SELECT seven, animal, COUNT(*) FROM students WHERE seven = '7' GROUP BY animal;

CREATE TABLE smallest_int_count AS
  SELECT smallest, COUNT(*) as total FROM students GROUP BY smallest ORDER BY total DESC;
