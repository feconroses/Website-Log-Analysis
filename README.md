# About

Python script that uses psycopg2 to query a mock PostgreSQL database for a fictional news website to create reports on different visitor stats.

This script is useful to answer the following questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

# Requirements

To run this script, the following resources are needed: 

* [Vagrant](https://www.vagrantup.com/downloads.html)
* [Virtualbox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)

You can download the Vagrantfile to configure the virtual machine [here](https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile)

This file will set up and run the project in an environment with the following requirements:

* Python: 3.5.2
* PostgreSQL
* psycopg2

Once you have installed Vagrant and Virtualbox, run the Vagrantfile to configure the environment. Then, run vagrant up to start the virtual machine and vagrant ssh to connect to it.

# Running the script

First, download the data related to this project from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.

The newsdata database has 3 tables: articles, log, and authors. 

To build the reporting tool, you'll need to load the site's data into your local database. To load the data, cd into the vagrant directory and use the command: 
`psql -d news -f newsdata.sql`

Then run: `psql -d news -f create_views.sql` to import the SQL views to the news database. You'll would only need to do this once, when you initially set up the database.

Finally, run the following file from the command line:
`python log-analysis.py`

Once you ran this command, the program will start processing the database to answering the questions mentioned above.

# How it works

For the first question, we'll answer it by doing a count of the join of articles and log tables, which are joined on the articles.slug and the path.log (path needs to be modified so it has the same format as slug). 

For the second question, we'll use a called normalized_log_path_for_authors that normalizes the path of the authors table, and then a function makes a count of grouping articles by title in this view.

For the third question, we'll use 3 views:
- requests_day_view: counts the number of requests per day
- error_counts_view: counts the number of errors per day
- joined_requests_and_errors: join both tables and order them by date

Finally, we convert the date to a readable form, calculate the error rate per day and filter by those days where more than 1 percent of requests lead to errors.

Check out example-output.txt to see an example of my program's output.