drop table if exists openings;

create table openings(
	id serial primary key,
	title text,
	jobId text,
	companyName text,
	t_s text,
	jdURL text,
	jobDescription text
	);
