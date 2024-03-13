-- Creates a table id_not_null with description id and name
-- The default value of id is set to 1
CREATE TABLE IF NOT EXISTS id_not_null (`id` INT DEFAULT 1, `name` VARCHAR(256));
