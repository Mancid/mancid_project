from flask import jsonify
from backend.dict_url import dict_url
from backend.parse_xml import xml_parse_url

route = '/api/parking'


def view():
    res = {}
    for parking, url in dict_url().items():
        res[parking] = xml_parse_url(url)
    return jsonify(res)
