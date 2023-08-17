-- Display top 3 hottest cities from temperatures.sql during the months of
-- July and August.
SELECT `city`, AVG(`value`) AS `avg_temp` FROM temperatures
       WHERE `month` BETWEEN 7 AND 8
       GROUP BY `city`
       ORDER BY `avg_temp` DESC
       LIMIT 3;
