import logging
import urllib.request
import xml.etree.ElementTree as ET


def xml_parse_url(url):
    """This function return all values in
    the url, with the library xml.etree. ElementTree
    we recover the data on the xlm url adding the
    result in list
    :return: dict with values total, free , status of
    all velo borne.
    :rtype: dict
    """
    open_url = urllib.request.urlopen(url).read()
    logging.debug("initializing the variable %s for read the url", open_url)
    xml_data = ET.fromstring(open_url)
    logging.debug("transform the url in str")
    res = {}
    for elem in xml_data[0]:
        name = elem.get("na")[4:]
        pos = elem.get("la") + ", " + elem.get("lg")
        dispo = elem.get("av")
        free = elem.get("fr")
        res[name] = {"pos": pos, "dispo": int(dispo), "free": int(free)}
    return res


def dict_velo(dict_url):
    """ This function take all name of parking
    and add in a dict with the values in xml_parse_url

    :returns: dictionnary with all parking and all values from xml url
    :rtype: dict
    """
    data = []
    for name, value in dict_url.items():
        res = value
        res["name"] = name
        data.append(res)
    return data
