import logging


def insert_db(database, data, *conf):
    """This function insert rows in the database
    mongodatabase

    :returns: inserts rows in the database
    :rtype: rows in database
    """
    logging.info("%s this is the data add in database", data)
    return database.insert(data)
