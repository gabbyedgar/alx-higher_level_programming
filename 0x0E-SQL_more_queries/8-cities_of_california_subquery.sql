-- List all cities of CA that can be found in database `hbtn_0d_usa`
SELECT `id`, `name` FROM cities
       WHERE cities.`state_id` =
       	     (SELECT `id` FROM states
	     	     WHERE `name` = "California")
       ORDER BY `id` ASC;
