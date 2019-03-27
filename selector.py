import psycopg2
from setup.authfile import dbname, dbuser, userPass


def query(queryStatement):
  conn = psycopg2.connect(database=dbname, user=dbuser, password=userPass)
  # the above needs to be fixed
  cursor = conn.cursor()
  cursor.execute(queryStatement)
  select = cursor.fetchall()
  conn.close()
  return select


def runSQLFile(filePath):
  with open(filePath, 'r') as file:
      select = file.read()
  return query(select)


def parsePopAuthor():
  authorList = runSQLFile('queries/popAuthor.sql')
  print('\nTop Authors:')
  for author in authorList:
      print("  {} - {} veiws".format(author[0], int(author[1])))


def parsePopArticle():
  articleList = runSQLFile('queries/popArticle.sql')
  print('\nTop 3 Articles')
  for article in articleList:
      print("  {} - {} veiws".format(article[0], int(article[1])))


def parseHigh404():
  list404 = runSQLFile('queries/high404.sql')
  print('\nDays with more than 1.5% of 404 responses:')
  for error in list404:
      day = str(error[-1])[:str(error[-1]).index(' ')]
      percent = str(float(error[0]))
      percent = percent[:percent.index('.')+3]
      print("  {}: {}% 404 Responses".format(day, percent))


if __name__ == "__main__":
    parsePopAuthor()
    parsePopArticle()
    parseHigh404()
