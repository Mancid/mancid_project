import sqlite3


def all_infos():
    res = []
    c = conn.cursor()
    c.row_factory = sqlite3.Row
    c.execute("""SELECT * FROM Parking""")
    for row in c.fetchall():
        res.append(dict(row))
    return res


if __name__ == "__main__":
    conn = sqlite3.connect('parking.db')
