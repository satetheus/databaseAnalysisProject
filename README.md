# fsnd-1
A tool for analysis of the newsdata database.

## Dependencies:
  | Dependency | Supported Version |
  | :--------: | :---------------: |
  | Python 3   | 3.7.2             |
  | PostgreSQL | 10.7              |
  | psycopg2   | 2.7.7             |


## Setup:
  1. Run "setup/views.sql" to setup the required views for this tool.
    - Contents of setup/views.sql:
    ``` sql
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
    ```

  2. Install all the modules from "setup/requirements.txt", you can run the following command:
       ```bash
       pip install -r setup/requirements.txt
       ```

  3. Fill out the values in setup/authfile.py to match the values for the PostgreSQL table:


  | Variable name | Variable values        |
  | :------------ | :-------------         |
  | dbname        | Database to connect to |
  | dbuser        | PostgreSQL username    |
  | userPass      | User password          |


  Example:
```python
dbname="my_database"
dbuser="me!"
userPass="imnottellingyou"
```


## Running from commandline/terminal:
Windows:
  1. Open the directory fsnd-1 is installed in.
  2. Run:
   ```bash
   python selector.py
  ```

Mac:
  1. Open the directory fsnd-1 is installed in.
  2. Run:
  ```bash
  python selector.py
  ```

Linux:
  1. Open the directory fsnd-1 is installed in.
  2. Run:
   ```bash
   selector.py
   ```

## Example Output:

```
Top Authors:
  Ursula La Multa - 512805 veiws
  Rudolf von Treppenwitz - 427781 veiws
  Anonymous Contributor - 171762 veiws
  Markoff Chaney - 85387 veiws

Top 3 Articles:
  Candidate is jerk, alleges rival - 342102 veiws
  Bears love berries, alleges bear - 256365 veiws
  Bad things gone, say good people - 171762 veiws

Days with more than 1% of responses ending in 404:
  2016-07-17: 2.27% 404 Responses
```
