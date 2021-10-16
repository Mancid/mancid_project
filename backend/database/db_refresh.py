from backend.function_park.dict_url import dict_url
from backend.function_tram.dict_tram import dict_tram
from backend.function_park.parse_xml import create_dict
from backend.database import db_mongo_park, db_mongo_tram
from backend.variable import HOST, PASSWORD, PARKING_SERVER, TRAM_SERVER


def refresh():
    """ This function refresh the database in atlas db

    :returns: refresh to atlas mongo db
    :rtype: database
    """
    print("[*] Start of databases initialization")
    data = create_dict(dict_url("url.ini"))
    db_mongo_park.main_db(HOST, PASSWORD, PARKING_SERVER,
                          data, "parking", "url.ini")
    print("   [*] Database Parking initialized")
    data = dict_tram()
    db_mongo_tram.main_db(HOST, PASSWORD, TRAM_SERVER, data, "tram")
    print("   [*] Database Tram initialized")
    print("[*] End of databases initialization")
