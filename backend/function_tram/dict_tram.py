from backend.function_tram.tools import download_csv, parse_csv
from backend.function_tram.config import TAM_ADRESS


def dict_tram():
    """Create a dictionnary with element of csv_file

    :returns: dictionnary with all tram
    :rtype: dict
    """
    csv = download_csv()
    data = []

    for row in parse_csv(csv):
        if int(row['route_short_name']) <= 4:
            for station, adress in TAM_ADRESS.items():
                if station == row['stop_name']:
                    data.append({'Ligne': row['route_short_name'],
                                 'Station': row['stop_name'],
                                 'Direction': row['trip_headsign'],
                                 'Delai': round(int(row['delay_sec'])/60),
                                 'Adresse': adress
                                 })
    return data
