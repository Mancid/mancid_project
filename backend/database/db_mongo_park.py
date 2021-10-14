import logging
from backend.database.db_remove import remove_db
from backend.database.db_connect import connect_db
from backend.function_park.dict_url import dict_url
from backend.function_park.parse_xml import create_dict


def insert_db(database, conf):
    """This function insert rows in the database
    mongodatabase

    :returns: inserts rows in the database
    :rtype: rows in database
    """
    values = create_dict(dict_url(conf))
    logging.info("%s this is the values add in database", values)
    return database.insert(values)


def result_db(database):
    """ This function return the result with all
    name in parking. They return a dict

    :returns: a dict with all rows in database
    :rtype: dict
    """
    return list(database.find({}, {"_id": 0}))


def main_db(host, password, server, table, conf):
    """This is the main function to call
    all other functions

    :returns: connection, remove, insert and result
    :rtype: main function
    """
    my_db = connect_db(host, password, server, table)
    remove_db(my_db)
    insert_db(my_db, conf)
