-- lists all genres NOT of the Dexter show

SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.name NOT IN (
	SELECT tv_genres.name
	FROM tv_genres 
	INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
	INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
	WHERE tv_shows.title  = "Dexter") -- returns genres linked to Dexter
ORDER BY tv_genres.name;
