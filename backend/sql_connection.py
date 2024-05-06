import mysql.connector

__cnx = None 
# its a global variable.


def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root',password='Roots@12345', host = '127.0.0.1', database = 'grocery_store')

    return __cnx