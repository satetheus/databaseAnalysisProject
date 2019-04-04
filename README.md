# fsnd-1
A tool for analysis of the newsdata database. This connects to the database, then runs queries to find the authors with the most views, the 3 articles with the most views, & days with more than 1% of it's responses being 404. Output when ran from the commandline/terminal is for human readability, not interaction with other programs or tools.

## Dependencies:
  | Dependency | Supported Version |
  | :--------: | :---------------: |
  | Python 3   | 3.7.2             |
  | PostgreSQL | 10.7              |
  | psycopg2   | 2.7.7             |


## Setup:
  1. #### Download newsdata.sql file:
    https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

  2. #### Import database:

     if using vagrant/virtualbox:
      - move newsdata.sql to vagrant folder
      - cd into vagrant folder
      - run `psql -U [userName] -f newsdata.sql`

     else:
      - cd into directory containing `newsdata.sql`
      - run `psql -U [userName] -f newsdata.sql`

  3. #### Clone the fsnd-1 repository.
  You can run:
  ```bash
  git clone https://github.com/satetheus/fsnd-1
  ```
  4. #### Setup views
     You can run the following command from the fsnd-1 directory:
     ```bash
     psql -U [userName] -f setup/views.sql
     ```

     Or you can run the contents of `setup/views.sql` from PostgreSQL.

  Contents of `setup/views.sql`:

```sql
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

  5. #### Install requirements from `setup/requirements.txt`
  You can run the following command:
       ```bash
       pip install -r setup/requirements.txt
       ```

  6. #### Fill out authorization
  Fill out the values in setup/authfile.py to match the values for the PostgreSQL table:


  | Variable name | Variable values        |
  | :------------ | :-------------         |
  | dbname        | Database to connect to |
  | dbuser        | PostgreSQL username    |
  | userPass      | User password          |

  ##### Example:
  ```python
  dbname="my_database"
  dbuser="me!"
  userPass="imnottellingyou"
  ```


## Running from commandline/terminal:
#### Windows:
  1. Open the directory fsnd-1 is installed in.
  2. Run:
   ```bash
   python selector.py
  ```

#### Mac:
  1. Open the directory fsnd-1 is installed in.
  2. Run:
  ```bash
  python selector.py
  ```

#### Linux:
  1. Open the directory fsnd-1 is installed in.
  2. Run:
   ```bash
   selector.py
   ```

## Example Output:

```
Top Authors:
  Ursula La Multa - 507594 veiws
  Rudolf von Treppenwitz - 423457 veiws
  Anonymous Contributor - 170098 veiws
  Markoff Chaney - 84557 veiws

Top 3 Articles:
  Candidate is jerk, alleges rival - 338647 veiws
  Bears love berries, alleges bear - 253801 veiws
  Bad things gone, say good people - 170098 veiws

Days with more than 1% of responses ending in 404:
  17/07/2016: 2.28% 404 Responses
```
