-- List all shows and their associated genres
SELECT tv_shows.title AS title,
       tv_genres.name AS name
       FROM tv_shows
       LEFT JOIN tv_show_genres
       ON tv_shows.id = tv_show_genres.show_id
       LEFT JOIN tv_genres
       ON tv_genres.id = tv_show_genres.genre_id
       ORDER BY tv_shows.title ASC, tv_genres.name ASC;
