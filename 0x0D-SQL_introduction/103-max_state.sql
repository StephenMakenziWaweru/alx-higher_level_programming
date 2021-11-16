-- displays the max temp of each state
-- ordered by State Name
SELECT state, MAX(value) max_temp FROM temperatures GROUP BY state ORDER BY state;
