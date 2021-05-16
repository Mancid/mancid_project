import xml.etree.ElementTree as ET
import urllib.request
import logging
from backend.function.dict_url import dict_url


def xml_parse_url(url):
    """This function return all values in
    the url, with the library xml.etree. ElementTree
    we recover the data on the xlm url adding the
    result in list
    """
    open_url = urllib.request.urlopen(url).read()
    logging.debug(f"initializing the variable {open_url} for read the url")
    xml_data = ET.fromstring(open_url)
    logging.debug('transform the url in str')
    res = {}
    for elem in xml_data.findall('Total'):
        logging.info(f"add value total {xml_data.findall('Total')}")
        res['Total'] = elem.text
    for elem in xml_data.findall('Free'):
        logging.info(f"add value total {xml_data.findall('Free')}")
        res['Free'] = elem.text
    for elem in xml_data.findall('DateTime'):
        logging.info(f"add value total {xml_data.findall('DateTime')}")
        elem = elem.text.split("T")[-1]
        res['Heure'] = elem[0:8]
    for elem in xml_data.findall('Status'):
        logging.info(f"add value total {xml_data.findall('Status')}")
        res['Status'] = elem.text
    return res


def create_dict(url):
    mydict = {}
    res = []
    for parking, url in dict_url().items():
        mydict[parking] = xml_parse_url(url)
    res.append(mydict)
    return res
