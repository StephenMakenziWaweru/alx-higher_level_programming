-- lists all cities in db

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
WHERE cities.state_id = states.id;
