from backend.function_park.dict_url import dict_url
from backend.function_tram.dict_tram import dict_tram
from backend.function_park.parse_xml import dict_parking
from backend.function_velo.xml_parse import dict_velo, xml_parse_url
from backend.database.db_main import main_db
from backend.variable import HOST, PASSWORD
from backend.variable import PARKING_SERVER, TRAM_SERVER, VELO_SERVER
from backend.variable import URL_VELOCITY


def refresh():
    """ This function refresh the database in atlas db

    :returns: refresh to atlas mongo db
    :rtype: database
    """
    print("[*] Start of databases initialization")
    data = dict_parking(dict_url("url.ini"))
    main_db(HOST, PASSWORD, PARKING_SERVER, data, "parking")
    print("   [*] Database Parking initialized")
    data = dict_tram()
    main_db(HOST, PASSWORD, TRAM_SERVER, data, "tram")
    print("   [*] Database Tram initialized")
    data = dict_velo(xml_parse_url(URL_VELOCITY))
    main_db(HOST, PASSWORD, VELO_SERVER, data, "velo")
    print("   [*] Database Vélo initialized")
    print("[*] End of databases initialization")
