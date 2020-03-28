CREATE TABLE courses(professor, course, semester);
INSERT INTO courses VALUES ("Dan", '61c','sp19');
INSERT INTO courses VALUES ("John",'61a','fa18');
INSERT INTO courses VALUES('Dan','10','fa18');
INSERT INTO courses VALUES ('Josh','61b','sp18'),("John",'61a','sp18'),("John",'61a','fa17');
INSERT INTO courses VALUES ('Paul','61a','fa17');
INSERT INTO courses VALUES ('Paul','61a','sp17'),('John','data8','sp17'),('Josh','61b','sp17');
INSERT INTO courses VALUES ('Satish','70','sp17'),('Nic','61c','sp17'),('Gerald','61c','sp17');
 # 6.1
CREATE TABLE num_taught(professor, course, times);
insert into num_taught select a.professor, a.course, count(*) 
	from courses as a, courses as b where a.professor = b.professor and a.course=b.course 
		and a.semester= b.semester group by a.professor, a.course;
# 6.2
select a.professor, b.professor, a.course from num_taught as a, num_taught as b 
	where a.professor>b.professor and a.times = b.times and a.course = b.course;
    
    #6.3
select a.professor, b.professor, count(*) from courses as a, courses as b 
	where a.professor<b.professor and a.course = b.course and a.semester = b.semester group by a.semester having count(*)>1;