CREATE OR REPLACE VIEW times AS
  SELECT articles.title AS article,
         authors.name AS author,
         log.time as viewtime
  FROM log
  JOIN articles
  ON log.path LIKE CONCAT('%', articles.slug, '%')
  JOIN authors
  ON authors.id = articles.author
