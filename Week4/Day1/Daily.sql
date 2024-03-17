-- CREATE TABLE actors(
--  actor_id SERIAL PRIMARY KEY,
--  first_name VARCHAR (50) NOT NULL,
--  last_name VARCHAR (100) NOT NULL,
--  age DATE NOT NULL,
--  number_oscars SMALLINT NOT NULL
-- )
-- In this exercise we will be using the actors table from todays lesson.
-- 1. Count how many actors are in the table.
-- 2. Try to add a new actor with some blank fields. What do you think the outcome will be ?
select count(*)
from actors
insert into actors (first_name, last_name, age, number_oscars)
values (,,) ERROR: Failing row contains (1,,, null, null).null value in column "age" of relation "actors" violates not - null constraint ERROR: null value in column "age" of relation "actors" violates not - null constraint SQL state: 23502 Detail: Failing row contains (1,,, null, null).