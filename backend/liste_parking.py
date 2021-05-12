import logging
import sqlite3


def liste_parking():
    c.execute("""
    SELECT Nom FROM Parking
    """)
    Nom = []
    for row in c:
        Nom.append(row[0])
    liste_parking = sorted(Nom)
    return liste_parking


if __name__ == "__main__":
    conn = sqlite3.connect('parking.db')
    c = conn.cursor()
    liste_parking()
    conn.commit()
    conn.close()