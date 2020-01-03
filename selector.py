#!/usr/bin/env python3
import psycopg2
from setup.authfile import dbname, dbuser, userPass


def runSQLFile(filePath):
    """
    Function:
      Connects to database as user specified in setup/authfile,
      then runs a given statement.
    Inputs:
      File path to an sql file.
    Outputs:
      Raw output from PostgreSQL as list.
    """
    with open(filePath, 'r') as file:
        queryStatement = file.read()
    connection = psycopg2.connect(
        database=dbname, user=dbuser, password=userPass)
    cursor = connection.cursor()
    cursor.execute(queryStatement)
    select = cursor.fetchall()
    connection.close()
    return select


def parsePopAuthor():
    """
    Function:
      Runs runSQLFile function for the statements in queries/popAuthor.sql,
      & cleans the output into human readable format.
    Inputs:
      None
    Outputs:
      List of strings for the top authors, starting with a header at
      parsedList[0], & a set of strings detailing article name with number
      of views.
    """
    formattedAuthors = ['\nTop Authors:']
    authors = runSQLFile('queries/popAuthor.sql')
    for author in authors:
        formattedAuthors.append(
            "  {} - {} veiws".format(author[0], int(author[1])))
    return formattedAuthors


def parsePopArticle():
    """
    Function:
      Runs runSQLFile function for the statements in queries/popArticle.sql,
      & cleans the output into human readable format.
    Inputs:
      None
    Outputs:
      List of strings for the top 3 articles, starting with a header at
      parsedList[0], & 3 strings detailing author name with number of views.
    """
    parsedList = ['\nTop 3 Articles:']
    articleList = runSQLFile('queries/popArticle.sql')
    for art in articleList:
        parsedList.append("  {} - {} veiws".format(art[0], int(art[1])))
    return parsedList


def parseHigh404():
    """
    Function:
      Runs the runSQLFile function for the statements in queries/high404.sql,
      & cleans the output into human readable format.
    Inputs:
      None
    Outputs:
      List of strings for the high 404 response days, starting with a
      header at parsedList[0], & a set of days with above 1.5% 404 responses.
    """
    parsedList = ['\nDays with more than 1% of responses ending in 404:']
    list404 = runSQLFile('queries/high404.sql')
    for err in list404:
        parsedList.append("  {}: {}% 404 Responses".format(err[-1], err[0]))
    return parsedList


if __name__ == "__main__":
    authors = parsePopAuthor()
    [print(x) for x in authors]

    articles = parsePopArticle()
    [print(x) for x in articles]

    errors = parseHigh404()
    [print(x) for x in errors]
