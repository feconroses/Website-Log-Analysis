/* view for normalizing normalize paths from log + join authors // Answer 2 */
CREATE VIEW normalized_log_path_for_authors 
AS SELECT articles.title, articles.author, authors.name,
articles.slug, log.time
FROM articles JOIN log
ON REPLACE(log.path, '/article/', '') = articles.slug
JOIN authors
ON authors.id = articles.author;

/* view for grouping requests per day // Answer 3 */
CREATE VIEW requests_day_view AS
SELECT count(*) AS requests, time::date AS new_time
FROM log
GROUP BY new_time
ORDER BY new_time;

/* view for counting errors per day // Answer 3 */
CREATE VIEW error_counts_view AS
SELECT count(*) AS error_count, time::date AS new_time
FROM log
WHERE status != '200 OK'
GROUP BY new_time
ORDER BY new_time;

/* view for joining both tables (requests per day and error per day) // Answer 3 */
CREATE VIEW joined_requests_and_errors AS
SELECT requests_day_view.new_time,
requests_day_view.requests,
error_counts_view.error_count
FROM requests_day_view JOIN error_counts_view
ON requests_day_view.new_time
= error_counts_view.new_time
ORDER BY new_time;
