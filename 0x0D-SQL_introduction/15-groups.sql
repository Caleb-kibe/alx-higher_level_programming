-- Lists the number of records with the same score in the second_table
-- Displays the score with the number of records of this score with the label `number`
-- The list is sorted by the number of records in descending order
SELECT score, COUNT(*) AS `number` FROM second_table GROUP BY score ORDER BY number DESC;
