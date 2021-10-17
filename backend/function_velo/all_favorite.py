from backend.database.db_result import result_db
from backend.database.db_connect import connect_db


def all_favorite(host, password, veteo_server, table):
    res = []
    connection_db = connect_db(host, password, veteo_server, table)
    for dico in result_db(connection_db):
        res.append(dico["name"])
    return res
