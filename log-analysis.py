"""!/usr/bin/env python3."""
# coding: utf-8
# by Federico Pascual
# Udacity rocks

import psycopg2

'''
1. What are the most popular three articles of all time? Which articles
have been accessed the most? Present this information as a sorted list
with the most popular article at the top.

Example:

"Princess Shellfish Marries Prince Handsome" — 1201 views
"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
"Political Scandal Ends In Political Scandal" — 553 views
'''

results = ''


def execute_query(query):
    """Helper function for running the SQL queries."""
    conn = psycopg2.connect("dbname=news")
    cursor = conn.cursor()
    cursor.execute(query)
    global results
    results = cursor.fetchall()
    conn.close()


def most_popular_articles():
    """function for finding the 3 most popular articles."""
    # count by title
    query = """
        SELECT articles.title, count(*) AS views
        FROM articles JOIN log
        ON REPLACE(log.path, '/article/', '') = articles.slug \
        GROUP BY articles.title
        ORDER BY views DESC;"""

    execute_query(query)

    # print question 1
    print('1. What are the most popular three articles of all time? \
Which articles have been accessed the most? \n')

    # print result of the top 3 articles
    article_count = 0
    for article in results:
        article_count += 1
        if article_count <= 3:
            print(str((article)[0]) + ' — ' + str((article)[1]) + ' views')
        else:
            break


'''
2. Who are the most popular article authors of all time? That is,
when you sum up all of the articles each author has written, which
authors get the most page views? Present this as a sorted list with
the most popular author at the top.

Example:

Ursula La Multa — 2304 views
Rudolf von Treppenwitz — 1985 views
Markoff Chaney — 1723 views
Anonymous Contributor — 1023 views
'''


def most_popular_authors():
    """function for finding the most popular authors."""
    # count views grouped by title and authors name
    query = """
        SELECT normalized_log_path_for_authors.name,
        count(*) AS views
        FROM normalized_log_path_for_authors
        GROUP BY normalized_log_path_for_authors.name
        ORDER BY views DESC;
        """

    execute_query(query)

    # print question 2
    print('\n2. Who are the most popular article authors of all \
time?\n')

    # print result
    for article in results:
        print(str((article)[0]) + ' — ' + str(
            (article)[1]) + ' views')


'''
3. On which days did more than 1% of requests lead to errors?
The log table includes a column status that indicates the HTTP
status code that the news site sent to the user's browser.
(Refer to this lesson for more information about the idea of
HTTP status codes.)

Example:

July 29, 2016 — 2.5% errors

'''


def most_common_error():
    """function for finding the most common error."""
    query = """
        SELECT to_char(new_time,'FMMonth dd, yyyy') AS converted_time,
        requests, error_count,
        CAST(error_count AS float) / CAST(requests AS float)
        * 100 AS percentaje_of_errors
        FROM joined_requests_and_errors;
        """

    execute_query(query)

    # print question 3
    print('\n3. On which days did more than 1 percent of requests \
lead to errors?\n')

    # print result
    for elem in results:
        if elem[3] > 1:
            print(elem[0], round(elem[3], 1), '% errors')


'''
running everything together
'''


def main():
    """run everything."""
    most_popular_articles()
    most_popular_authors()
    most_common_error()


if __name__ == '__main__':
    # make sure to only run when this program is executed directly
    main()
