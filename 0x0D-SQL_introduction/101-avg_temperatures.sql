-- import dump into hbtn_0c_0
-- displays avg temp by city ordered by temp (desc)
SELECT city, AVG(value) avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
