create table if not exists tourguide.templates
(
	title varchar(100) null,
	description longtext null,
	id int auto_increment
		primary key
);
