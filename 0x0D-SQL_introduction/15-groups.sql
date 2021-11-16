-- lists the number of records with same score
-- display score and number
SELECT score, COUNT(*) number FROM second_table GROUP BY score ORDER BY number DESC;
