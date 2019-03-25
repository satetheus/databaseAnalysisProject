SELECT authors.name,
       COUNT(log.time)
FROM log
JOIN articles
ON log.path LIKE CONCAT('%', articles.slug, '%')
JOIN authors
ON authors.id = articles.author
GROUP BY 1
ORDER BY 2 DESC


SELECT articles.title,
       COUNT(log.time)
FROM log
JOIN articles
ON log.path LIKE CONCAT('%', articles.slug, '%')
GROUP BY 1
ORDER BY 2 DESC

/*
WITH trunc_date AS (
  SELECT SUM(CASE log.status like '200%' WHEN 't' THEN 1
         ELSE 0
         END) AS good,

         SUM(CASE log.status like '404%' WHEN 't' THEN 1
         ELSE 0
         END) AS bad,

         DATE_TRUNC('day', log.time) AS day
  FROM log
  GROUP BY 3)


SELECT bad/(bad+good+0.0)*100 as percent,
       good,
       bad,
       day
FROM trunc_date
WHERE bad/(bad+good+0.0) > 0.01
*/
