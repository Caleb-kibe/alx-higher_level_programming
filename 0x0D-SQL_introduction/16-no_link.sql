-- Lists all records of the second_table
-- Does not list row without a name value
-- Displays the score and the name in that order
-- Records are displayed in descending order
SELECT score, name FROM second_table WHERE name != "" ORDER BY score DESC;
