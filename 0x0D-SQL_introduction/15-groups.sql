-- Count all number of instances of each score in `second_table`
SELECT `score`, COUNT(`score`) AS "number"
       FROM second_table
       GROUP BY `score`
       ORDER BY `score` DESC;
