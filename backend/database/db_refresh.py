import os
from backend.database import db_mongo_park, db_mongo_tram
from backend.variable import HOST, PASSWORD, PARKING_SERVER, TRAM_SERVER


def refresh():
    print("[*] Start of databases initialization")
    db_mongo_park.main_db(HOST, PASSWORD, PARKING_SERVER, "parking", "url.ini")
    print("   [*] Database Parking initialized")
    db_mongo_tram.main_db(HOST, PASSWORD, TRAM_SERVER, "tram")
    print("   [*] Database Tram initialized")
    print("[*] End of databases initialization")
