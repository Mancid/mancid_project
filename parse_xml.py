import xml.etree.ElementTree as ET
import urllib.request
import dict_url


def xml_parse_url(url):
    open_url = urllib.request.urlopen(url).read()
    xml_data = ET.fromstring(open_url)
    res = []
    for elem in xml_data.findall('Status'):
        res.append(elem.text)
    for elem in xml_data.findall('Free'):
        res.append(elem.text)
    for elem in xml_data.findall('Total'):
        res.append(elem.text)
    return res


def parking_parse():
    for parking, url in dict_url.dict_url().items():
        return parking, xml_parse_url(url)
