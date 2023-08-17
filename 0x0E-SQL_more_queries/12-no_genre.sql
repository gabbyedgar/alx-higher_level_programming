-- List all shows without an associated genre from `hbtn_0d_tvshows`
SELECT tv_shows.title AS title,
       tv_show_genres.genre_id AS genre_id
       FROM tv_shows LEFT JOIN tv_show_genres
       ON tv_shows.id = tv_show_genres.show_id
       WHERE tv_show_genres.genre_id IS NULL
       ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
