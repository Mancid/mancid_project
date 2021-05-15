from backend.function.dict_url import dict_url
from backend.function.parse_xml import xml_parse_url
from .connect_db import connect


def update_table(db):
    conn, c = connect(db)
    for parking, url in dict_url().items():
        rows = (xml_parse_url(url)[0], xml_parse_url(url)[1],
                xml_parse_url(url)[2], xml_parse_url(url)[3], parking)
        sql = """UPDATE Parking SET Total=?,Free=?,Heure=?,Status=?
                 WHERE Nom=?"""
        c.execute(sql, rows)
    conn.commit()
    conn.close()
