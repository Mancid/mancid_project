from backend.function.dict_url import dict_url
from backend.function.parse_xml import xml_parse_url
from .connect_db import connect


def update_table(database):
  """
  this function allows to update the database 'database'.
  """
  conn, cursor = connect(database)
  for parking, url in dict_url().items():
    cursor.execute("""UPDATE Parking SET Total=?,Free=?,Heure=?,Status=?
              WHERE Nom=?""", (xml_parse_url(url)[0], xml_parse_url(url)[1],
                               xml_parse_url(url)[2], xml_parse_url(url)[3],
                               parking))
  conn.commit()
  conn.close()
