import logging


def remove_db(database):
    """ This function remove all rows in database mongodatabase

    :returns: Remove all rows in database
    :rtype: remove
    """
    logging.info("remove all rows in database mongodatabase")
    return database.remove({})
