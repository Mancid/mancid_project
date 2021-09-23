from backend.database import db_mongo_park, db_mongo_tram


def refresh():
    print("[*] Start of databases initialization")
    db_mongo_park.main_db()
    print("   [*] Database Parking initialized")
    db_mongo_tram.main_db()
    print("   [*] Database Tram initialized")
    print("[*] End of databases initialization")
