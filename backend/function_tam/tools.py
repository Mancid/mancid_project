import requests
from backend.function_tam.config import TAM_CSV_URL


def download_csv():
    tam_data = requests.get(TAM_CSV_URL).text
    return tam_data


def parse_csv(csv):
    data = csv.strip().split('\r\n')
    header = [
        'course',
        'stop_code',
        'stop_id',
        'stop_name',
        'route_short_name',
        'trip_headsign',
        'direction_id',
        'departure_time',
        'is_theorical',
        'delay_sec',
        'dest_ar_code'
        ]

    structured_data = []

    for line in data[1:]:
        line_data = {}
        for index, value in enumerate(line.split(';')):
            line_data[header[index]] = value
        structured_data.append(line_data)
    if structured_data == []:
        structured_data = [{
                            'course': '',
                            'stop_code': '',
                            'stop_id': '',
                            'stop_name': 'FIN DU SERVICE',
                            'route_short_name': '0',
                            'trip_headsign': '',
                            'direction_id': '',
                            'departure_time': '',
                            'is_theorical': '',
                            'delay_sec': '',
                            'dest_ar_code': ''
                        },
                        {
                            'course': '',
                            'stop_code': '',
                            'stop_id': '',
                            'stop_name': 'FIN DU SERVICE',
                            'route_short_name': '99',
                            'trip_headsign': '',
                            'direction_id': '',
                            'departure_time': '',
                            'is_theorical': '',
                            'delay_sec': '',
                            'dest_ar_code': ''
                        }]

    return structured_data
