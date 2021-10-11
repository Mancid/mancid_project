import logging
from pymongo import MongoClient
from backend.function_park.parse_xml import create_dict
from backend.function_park.dict_url import dict_url


def connect_db(host, password, parking_server):
    """ This function connect in atlas a mongodb

    :returns: connection to atlas mongo db
    :rtype: connection string
    """
    client = MongoClient(f"mongodb+srv://{host}:{password}@{parking_server}?ssl=true&"\
                         "ssl_cert_reqs=CERT_NONE")
    logging.info(" %s client : ", client)
    conn = client.test
    logging.info(" your database : %s", conn)
    database = conn["Parking"]
    return database


def insert_rows(database, conf):
    """This function insert rows in the database
    mongodatabase

    :returns: inserts rows in the database
    :rtype: rows in database
    """
    values = create_dict(dict_url(conf))
    logging.info("%s this is the values add in database", values)
    return database.insert(values)


def remove(database):
    """ This function remove all rows in database mongodatabase

    :returns: Remove all rows in database
    :rtype: remove
    """
    logging.info("remove all rows in database mongodatabase")
    return database.remove({})


def result_database(database, conf):
    """ This function return the result with all
    name in parking. They return a dict

    :returns: a dict with all rows in database
    :rtype: dict
    """
    return list(database.find({}, {"_id": 0}))


def main_db(host, password, parking_server, conf):
    """This is the main function to call
    all other functions

    :returns: connection, remove, insert and result
    :rtype: main function
    """
    my_db = connect_db(host, password, parking_server)
    remove(my_db)
    insert_rows(my_db, conf)
