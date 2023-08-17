-- Load data from temperatures.sql into specified database
-- and display average temperature by city ordered by temperature.
SELECT `city`, AVG(`value`) AS `avg_temp`
       FROM temperatures
       GROUP BY `city`
       ORDER BY `avg_temp` DESC;
