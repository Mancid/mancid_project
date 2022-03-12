from flask import redirect, url_for, session
from backend.function_velo.meteo import data, conf
from backend.database.db_result import result_db
from backend.database.db_connect import connect_db


def dico_temps():
    liste = []
    dico = {}
    for v in data().values():
        dico["jour"] = v.split(",")[0][:10]
        dico["heure"] = v.split(",")[0][-8:]
        dico["temp"] = v.split(",")[1]
        dico["cond"] = v.split(",")[2]
        liste.append(dico)
    return liste


def favorite(host, password, server1, table1, server2, table2):
    connection_db1 = connect_db(host, password, server1, table1)
    connection_db2 = connect_db(host, password, server2, table2)
    for user in result_db(connection_db2):
        if session["email"] == user["email"]:
            for dico in result_db(connection_db1):
                if dico["name"] == user["favorite"]:
                    return dico["name"], dico["dispo"], dico["pos"]


def verdict():
    temp, cond = conf()
    print(temp, cond)
    if cond == "ciel dégagé" or cond == "partiellement nuageux" or cond == "peu nuageux" or cond == "nuageux":
        return f"Les conditions météos sont {cond}, il fait {temp}°C, tu peux prendre un vélo boug !"
    else:
        return f"Prend la voiture boug !!"
