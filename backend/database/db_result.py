import logging


def result_db(database):
    """ This function return the result of database.
    They return a dict

    :returns: a dict with all rows in database
    :rtype: dict
    """
    logging.info("The result of filter")
    return list(database.find({}, {"_id": 0}))
