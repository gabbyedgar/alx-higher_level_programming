-- List all genres not used to describe show Dexter from `hbtn_0d_tvshows
SELECT DISTINCT tv_genres.name
       	   FROM tv_genres
     INNER JOIN tv_show_genres
       	     ON tv_genres.id = tv_show_genres.genre_id
       	  WHERE tv_show_genres.genre_id
       	 NOT IN
		(SELECT tv_show_genres.genre_id
	   	   FROM tv_show_genres
	     INNER JOIN tv_shows
	     	     ON tv_show_genres.show_id = tv_shows.id
	   	  WHERE tv_shows.title = "Dexter")
       ORDER BY tv_genres.name ASC;
