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


SELECT ROUND(bad/(bad+good+0.0)*100, 2) as percent,
       good,
       bad,
       TO_CHAR(day, 'dd/mm/yyyy')
FROM trunc_date
WHERE bad/(bad+good+0.0) > 0.01
