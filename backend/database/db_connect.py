import logging
from pymongo import MongoClient


def connect_db(host, password, server, table):
    """ This function connect in atlas a mongodb

    :returns: connection to atlas mongo db
    :rtype: connection string
    """
    client = MongoClient(f"mongodb+srv://{host}:{password}@{server}?ssl=true&"\
                         "ssl_cert_reqs=CERT_NONE")
    logging.info(" %s client : ", client)
    conn = client.mancid
    logging.info(" your database : %s", conn)
    database = conn[table]
    return database
