SELECT author,
       SUM(number_of_views)
FROM times
GROUP BY 1
ORDER BY 2 DESC;
