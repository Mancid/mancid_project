from backend.function_tram.tools import download_csv, parse_csv
from backend.function_tram.config import TAM_ADRESS
# from tools import download_csv, parse_csv


def dict_tram():
    csv = download_csv()
    data = []

    for row in parse_csv(csv):
        if int(row['route_short_name']) <= 4:
          for station, adress in TAM_ADRESS.items():
            if station == row['stop_name']:
              data.append({'Ligne': row['route_short_name'],
                           'Station': row['stop_name'],
                           'Direction': row['trip_headsign'],
                           'Delai': str(round(int(row['delay_sec']) / 60)),
                           'Adresse': adress
                           })
    return data
