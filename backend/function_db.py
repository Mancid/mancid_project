import sqlite3
import logging


def all_infos():
    """ This function return all row
    in the database, with table name Parking
    """
    res = []
    c = conn.cursor()
    logging.info(f"connect to db with cursor {c}")
    c.row_factory = sqlite3.Row
    logging.info("initializing the cursor for return dict")
    c.execute("""SELECT * FROM Parking""")
    logging.debug("select all rows in database")
    for row in c.fetchall():
        res.append(dict(row))
        for i in res:
            print(i.get('Nom'))
    return res
    logging.info(f"this is the row in the database {res}")


if __name__ == "__main__":
    conn = sqlite3.connect('parking.db')
    print(all_infos())
