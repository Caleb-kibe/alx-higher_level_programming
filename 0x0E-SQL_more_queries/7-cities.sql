-- Creates a database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use the database
USE hbtn_0d_usa;
-- Creates a table cities
CREATE TABLE IF NOT EXISTS cities (`id` INT UNIQUE AUTO_INCREMENT, `state_id` INT, `name` VARCHAR(256), PRIMARY KEY(id), FOREIGN KEY(state_id) REFERENCES states(id));
