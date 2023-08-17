-- List all genres and their counts from `hbtn_0d_tvshows`
SELECT tv_genres.name AS genre,
       COUNT(tv_show_genres.genre_id) AS number_shows
       FROM tv_genres INNER JOIN tv_show_genres
       ON tv_genres.id = tv_show_genres.genre_id
       GROUP BY tv_genres.id
       ORDER BY number_shows DESC;
