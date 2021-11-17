-- creates db hbtn_9d_usa

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- create table states
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
	id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
	name VARCHAR(256) NOT NULL);	
