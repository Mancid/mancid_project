import logging
import sqlite3
from .connect_db import connect


def function_table(db):
    """ This function return all row
    in the database, with table name Parking
    """
    res, nom = [], []
    conn, c = connect(db)
    logging.info(f"connect to db with cursor {c}")
    c.row_factory = sqlite3.Row
    logging.info("initializing the cursor for return dict")
    c.execute("SELECT * FROM Parking")
    logging.debug("select all rows in database")
    for row in c.fetchall():
        res.append(dict(row))
        for i in res:
            title = (i.get('Nom'))
            if title not in nom:
                nom.append(title)
    conn.commit()
    conn.close()
    logging.info(f"this is the row in the database {res}")
    return res, nom
