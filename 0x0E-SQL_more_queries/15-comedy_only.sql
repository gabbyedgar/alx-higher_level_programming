-- List all comedy shows from `hbtn_0d_tvshows`
SELECT tv_shows.title AS title
       FROM tv_shows
       INNER JOIN tv_show_genres
       ON tv_shows.id = tv_show_genres.show_id
       INNER JOIN tv_genres
       ON tv_genres.id = tv_show_genres.genre_id
       WHERE tv_genres.name = "Comedy"
       ORDER BY title ASC;
