CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT dogs.name, sizes.size FROM dogs, sizes 
  WHERE sizes.min < dogs.height AND dogs.height <= sizes.max;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT a.child FROM 
  (SELECT parents.parent, parents.child FROM parents, dogs WHERE parents.child = dogs.name) AS a, dogs
	WHERE a.parent = dogs.name ORDER BY dogs.height DESC;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.child, b.child, c.size FROM parents AS a, parents AS b, size_of_dogs AS c, size_of_dogs AS d 
  WHERE a.child < b.child AND a.parent = b.parent AND a.child = c.name AND b.child = d.name AND c.size = d.size
  ORDER BY a.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT  siblings.child || ' and ' || siblings."child:1" || ' are ' || siblings.size || ' siblings' 
  FROM siblings;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height);

-- Add your INSERT INTOs here
INSERT INTO stacks_helper SELECT name, height, height FROM dogs;

------- solution
INSERT INTO stacks_helper
  SELECT a.dogs || ", " || b.name, a.stack_height + b.height, b.height
    FROM stacks_helper AS a, dogs AS b
    WHERE a.last_height < b.height;
---------

INSERT INTO stacks_helper SELECT a.dogs||', ' || b.dogs, a.stack_height + b.last_height, b.last_height 
FROM stacks_helper AS a, stacks_helper AS b 
WHERE a.dogs <> b.dogs AND a.last_height < b.last_height;

INSERT INTO stacks_helper SELECT  a.dogs||', ' || b.dogs, a.stack_height + b.last_height, b.last_height
FROM (SELECT * FROM stacks_helper as s WHERE s.dogs LIKE '%,%') AS a, 
	 (SELECT * FROM stacks_helper as s WHERE s.dogs NOT LIKE '%,%') as b
WHERE instr(a.dogs,b.dogs) = 0 AND a.last_height < b.last_height;
     
INSERT INTO stacks_helper SELECT  a.dogs||', ' || b.dogs, a.stack_height + b.last_height, b.last_height
FROM (SELECT * FROM stacks_helper as s WHERE length(s.dogs) - length(replace(s.dogs, ',', '')) = 2) AS a, 
	 (SELECT * FROM stacks_helper as s WHERE s.dogs NOT LIKE '%,%') as b
WHERE instr(a.dogs,b.dogs) = 0 AND a.last_height < b.last_height;

CREATE TABLE stacks AS
  SELECT dogs, stack_height FROM stacks_helper 
  WHERE stack_height > 170 ORDER BY stack_height;
