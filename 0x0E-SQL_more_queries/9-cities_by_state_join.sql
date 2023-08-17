-- List all cities in database `hbtn_0d_usa`
SELECT cities.id AS `id`,
       cities.name AS `name`,
       states.name AS `name`
       FROM cities INNER JOIN states ON cities.state_id = states.id
       ORDER BY cities.id ASC;
