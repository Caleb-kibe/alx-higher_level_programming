-- Creates a database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use the database
USE hbtn_0d_usa;
-- Creates a table states with columns id and name
CREATE TABLE IF NOT EXISTS states (`id` INT UNIQUE AUTO_INCREMENT, `name` VARCHAR(256), PRIMARY KEY(id));
