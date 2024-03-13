-- Creates a table unique_id with descriptin id and name
-- The id value is set to 1 and is made unique
CREATE TABLE IF NOT EXISTS unique_id (`id` INT DEFAULT 1 UNIQUE, `name` VARCHAR(256))
