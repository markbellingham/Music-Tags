"""Class for accessing the database."""
import pymysql

host = 'xxxxx'
user = 'xxxxx'
password = 'xxxxx'
db = 'xxxxx'

connection = pymysql.connect(host, user, password, db)
cursor = connection.cursor()


def insert(query):
    """Basic Insert function."""
    try:
        cursor.execute(query)
        connection.commit()
    except Exception:
        connection.rollback()


def insert_many(query, data):
    """Function to insert several records."""
    try:
        cursor.executemany(query, data)
        connection.commit()
    except Exception as error:
        connection.rollback()
        print(error)
