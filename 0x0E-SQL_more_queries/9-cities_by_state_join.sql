-- lists all cities in the database hbyn_0d_usa
-- Each record should display: cities.id - cities.name - states.name and the results are in ascending order by cities.id
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;
