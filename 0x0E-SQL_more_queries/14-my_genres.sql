-- lists all genres of the show Dexter
SELECT tv_genres.name AS name
	FROM tv_genres
	FULL JOIN tv_genres ON tv_shows.id = tv_show_genres.genre_id
	WHERE title = 'Dexter'
	ORDER BY name ASC;
