-- create table students(
-- 	id serial primary key,
-- 	last_name varchar(255) not null,
-- 	first_name varchar(255) not null,
-- 	birth_date date not null
-- );
-- INSERT INTO students (first_name,	last_name,	birth_date)
-- values
-- ('Marc',	'Benichou',	'02/11/1998'),
-- ('Yoan',	'Cohen',	'03/12/2010'),
-- ('Lea',	'Benichou',	'27/07/1987'),
-- ('Amelia',	'Dux',	'07/04/1996'),
-- ('David',	'Grez',	'14/06/2003'),
-- ('Omer',	'Simpson',	'03/10/1980')
-- ('Adir','Ozeri','10/11/1085')
-- ;
select *
from students;
select first_name,
    last_name
from students;
select first_name,
    last_name
from students
where id = 2;
select first_name,
    last_name
from students
where last_name = 'Benichou'
    and first_name = 'Marc';
select first_name,
    last_name
from students
where last_name = 'Benichou'
    OR first_name = 'Marc';
select first_name,
    last_name
from students
where first_name like '%a%';
select first_name,
    last_name
from students
where first_name like 'a%';
select first_name,
    last_name
from students
where first_name like '%a';
select first_name,
    last_name
from students
where first_name like '%a_';
select first_name,
    last_name
from students
where id in (1, 3);
select *
from students
where birth_date > '01/01/2000'