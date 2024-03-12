-- Lists all records with a score >= 10 in the second table
-- Displays both the score and the name in that order
-- Displays scores in order starting from the top score
SELECT `score`, `name` FROM second_table WHERE `score` >= 10 ORDER BY `score` DESC;
