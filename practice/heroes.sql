--CRUD datatypes : Create(create) Read(select) Update(update) Delete(delete)
--creating tables

create table heroes(
	--primary key : a unique id that cannot change is unique and not null
	id serial PRIMARY KEY,
	name text UNIQUE, --constraint : does not allow more than one row with the same name
	identity text,
	studio text,
	gender varchar(1),
	appearence integer
	);
	
--Inserting tables

insert into heroes (name, identity, studio, gender, appearence) values ('Superman', 'Clark Kent', 'DC', 'M', 1975);

insert into heroes (name, identity, studio, gender, appearence) values ('Batman', 'Bruce Wayne', 'DC', 'M', 1973);

insert into heroes (name, identity, studio, gender, appearence) values ('Black Widow', 'Natasha Romanov', 'Marvel', 'F', 1980);

insert into heroes (name, identity, studio, gender, appearence) values ('Iron Man', 'Tony Stark', 'Marvel', 'M', 1972);

insert into heroes (name, identity, studio, gender, appearence) values ('Scarlet Witch', 'Wanda Maximov', 'Marvel', 'F', 1995);

--QUERYING

--select fields from tables where condition;


select name, gender, studio from heroes where gender = 'M' and studio = 'Marvel';
select distinct studio from heroes;

--deleting from a table

delete from heroes where name = 'Superman'

--CONSTRAINTS

--adding constraints for an existing table
--alter table <table_name> add constraint <constraint_name(for reference not related)> <constraint(column)>;

alter table heroes add constraint constraint_name unique (name);
alter table heroes drop constraint constraint_name;

--alter columns
alter table heroes alter column name set not null;
alter table heroes alter column name drop not null;

--update a field

update heroes set name = 'Martian Manhunter', idetntity = 'John Jonz' wehere name = 'xSuperman';


-----------------------------------------------------------------------------------------------------

--Using foreign keys

create table studios(
	 
	id serial primary key,
	name text UNIQUE
	);

insert into studios (name) values ('Marvel');
insert into studios (name) values ('DC');

create table heroes(
	id serial primary key,
	name text UNIQUE,
	identity text,	
	studio text references studios(name) --foreign key
);

insert into heroes (name, identity, studio) values ('Superman', 'Clark Kent', 'DC');

insert into heroes (name, identity, studio) values ('Batman', 'Bruce Wayne', 'DC');

insert into heroes (name, identity, studio) values ('Black Widow', 'Natasha Romanov', 'marvel');

insert into heroes (name, identity, studio) values ('Iron Man', 'Tony Stark', 'Marvel');

insert into heroes (name, identity, studio) values ('Scarlet Witch', 'Wanda Maximov', 'Marvel');

--joining tables with conditions

superheroes=> select h.name, h.identity, s.name, s.id from heroes h, studios s where h.studio = s.name and s.id = 1;

--the above procedure created a many to one relation

--joining many to many

create table powers(
	id serial primary key,
	name text,
	description text
	);
	
insert into powers (name, description) values ('rich', 'extraordinarily rich');
insert into powers (name, description) values ('combat skills', 'highly developed combat skills');
insert into powers (name, description) values ('technology', 'huge arsenal of technology');
insert into powers (name, description) values ('magic', 'super natural powers');
insert into powers (name, description) values ('flight', 'ability to fly');

--joining table

create table hero_powers(
	heroes serial references heroes(id),
	powers serial references powers(id)
	);

--Superman Powers
insert into hero_powers (heroes, powers) values (1, 5);

--Batman Powers
insert into hero_powers (heroes, powers) values (2, 1);
insert into hero_powers (heroes, powers) values (2, 2);
insert into hero_powers (heroes, powers) values (2, 3);

--Ironman Powers
insert into hero_powers (heroes, powers) values (4, 1);
insert into hero_powers (heroes, powers) values (4, 3);
insert into hero_powers (heroes, powers) values (4, 5);

--Scarlet Witch Powers
insert into hero_powers (heroes, powers) values (5, 4);

--Scarlet Witch Powers
insert into hero_powers (heroes, powers) values (6, 2);
	
--joining

select h.name, p.name from heroes h, powers p , hero_powers hp where h.id = hp.heroes and p.id = hp.powers;

