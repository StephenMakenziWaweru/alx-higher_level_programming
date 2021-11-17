-- lists all the cities of California

SELECT id, name FROM cities
WHERE (SELECT id FROM states
	WHERE name = "California");
