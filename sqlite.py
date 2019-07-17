import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    '''Create a db connection to a SQLite db'''

    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()


#if __name__ == '__main__':
    #create_connection('/home/lblazok/App/baza.db')


def create_table(conn, create_table_sql):
    ''' Create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    '''

    try:
        c = conn.cursor()
        c.execute(create_table_sql) 
    except Error as e:
        print(e)

