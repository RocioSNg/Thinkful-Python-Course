drop table if exists person;

create table person (
	id int primary_key not null,
	name text not null,
	age int 
);

	insert into person values 
		(1, 'Bob', 22);
