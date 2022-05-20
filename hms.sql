CREATE DATABASE hms; 
USE hms;

-- 'id', 'name',  email', 'gender', 'contact', 'dob', 'address'

CREATE TABLE hospital(
	id int(100) primary key,
	name char(100) not null,
    email char(100),
    gender char(40) not null,
    contact char(40),
    dob char(40),
    address varchar(200)
);