from dict_url import dict_url
from parse_xml import xml_parse_url
import sqlite3


def update_table():
    for parking, url in dict_url().items():
        rows = (xml_parse_url(url)[0], xml_parse_url(url)[1],
                xml_parse_url(url)[2], xml_parse_url(url)[3], parking)
        sql = """UPDATE Parking SET Total=?,Free=?,Heure=?,Status=?
                 WHERE Nom=?"""
        c.execute(sql, rows)
    conn.commit()


if __name__ == "__main__":
    conn = sqlite3.connect('parking.db')
    c = conn.cursor()
    update_table()
    conn.commit()
