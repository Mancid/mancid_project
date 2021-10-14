#pylint: disable=E0401
import logging
from backend.database.db_remove import remove_db
from backend.database.db_connect import connect_db
from backend.function_tram.dict_tram import dict_tram


def insert_db(database):
    """This function insert rows in the database
    mongodatabase

    :returns: inserts rows in the database
    :rtype: rows in database
    """
    values = dict_tram()
    logging.info("%s this is the values add in database", values)
    return database.insert(values)


def result_db(database):
    """ This function return the result with all
    name in parking. They return a dict

    :returns: a dict with all rows in database
    :rtype: dict
    """
    return list(database.find({}, {"_id": 0}))


def main_db(host, password, server, table):
    """This is the main function to call
    all other functions

    :returns: connection, remove, insert and result
    :rtype: main function
    """
    my_db = connect_db(host, password, server, table)
    remove_db(my_db)
    insert_db(my_db)
