from backend.database.db_remove import remove_db
from backend.database.db_insert import insert_db
from backend.database.db_connect import connect_db


def main_db(host, password, server, data, table, conf):
    """This is the main function to call
    all other functions

    :returns: connection, remove, insert and result
    :rtype: main function
    """
    my_db = connect_db(host, password, server, table)
    remove_db(my_db)
    insert_db(my_db, data, *conf)
