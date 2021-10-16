import os
import logging
from backend.database import db_mongo_park, db_mongo_tram

HOST = os.environ["HOST_MONGO_DB"]
PASSWORD = os.environ["PASSWORD_MONGO_DB"]
PARKING_SERVER = os.environ["PARKING_SERVER"]
TRAM_SERVER = os.environ["TRAM_SERVER"]


def refresh():
    print("[*] Start of databases initialization")
    db_mongo_park.main_db(HOST, PASSWORD, PARKING_SERVER, "parking", "url.ini")
    print("   [*] Database Parking initialized")
    db_mongo_tram.main_db(HOST, PASSWORD, TRAM_SERVER, "tram")
    print("   [*] Database Tram initialized")
    print("[*] End of databases initialization")
