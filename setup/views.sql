CREATE OR REPLACE VIEW times AS
  SELECT articles.title AS article,
         authors.name AS author,
         COUNT(log.time) as number_of_views
  FROM log
  JOIN articles
  ON log.path LIKE CONCAT('%', articles.slug, '%')
  JOIN authors
  ON authors.id = articles.author
  GROUP BY 1, 2
