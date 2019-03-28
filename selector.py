import psycopg2
from setup.authfile import dbname, dbuser, userPass


def runSQLFile(filePath):
    with open(filePath, 'r') as file:
        queryStatement = file.read()
    conn = psycopg2.connect(database=dbname, user=dbuser, password=userPass)
    cursor = conn.cursor()
    cursor.execute(queryStatement)
    select = cursor.fetchall()
    conn.close()
    return select


def parsePopAuthor():
    parsedList = ['\nTop Authors:']
    authorList = runSQLFile('queries/popAuthor.sql')
    for author in authorList:
        parsedList.append("  {} - {} veiws".format(author[0], int(author[1])))
    return parsedList


def parsePopArticle():
    parsedList = ['\nTop 3 Articles:']
    articleList = runSQLFile('queries/popArticle.sql')
    for article in articleList:
        parsedList.append("  {} - {} veiws".format(article[0], int(article[1])))
    return parsedList


def parseHigh404():
    parsedList = ['\nDays with more than 1.5% of responses ending in 404:']
    list404 = runSQLFile('queries/high404.sql')
    for error in list404:
        day = str(error[-1])[:str(error[-1]).index(' ')]
        percent = str(float(error[0]))
        percent = percent[:percent.index('.')+3]
        parsedList.append("  {}: {}% 404 Responses".format(day, percent))
    return parsedList


if __name__ == "__main__":
    authors = parsePopAuthor()
    [print(x) for x in authors]

    articles = parsePopArticle()
    [print(x) for x in articles]

    errors = parseHigh404()
    [print(x) for x in errors]
