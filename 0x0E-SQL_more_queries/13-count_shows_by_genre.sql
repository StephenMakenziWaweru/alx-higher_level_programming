-- lists all genres and displays no. of shows linked to each

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows 
FROM tv_genres
INNER JOIN tv_show_genres 
WHERE tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
