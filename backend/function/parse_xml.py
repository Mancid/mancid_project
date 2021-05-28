import xml.etree.ElementTree as ET
import urllib.request
import logging
from backend.function.dict_url import dict_url


def xml_parse_url(url):
  """This function return all values in
  the url, with the library xml.etree. ElementTree
  we recover the data on the xlm url adding the
  result in list

  :return: dict with values total, free , status of 
  all parkings.
  :rtype: dict

  """
  open_url = urllib.request.urlopen(url).read()
  logging.debug("initializing the variable %s for read the url", open_url)
  xml_data = ET.fromstring(open_url)
  logging.debug("transform the url in str")
  res = {}
  for elem in xml_data.findall("Total"):
    logging.info("add value total %s", xml_data.findall("Total"))
    res["Total"] = int(elem.text)
  for elem in xml_data.findall("Free"):
    logging.info("add value total %s", xml_data.findall("Free"))
    res["Free"] = int(elem.text)
  for elem in xml_data.findall("Status"):
    logging.info("add value total %s", xml_data.findall("Status"))
    res["Status"] = elem.text
  return res


def create_dict(url):
  """
  This function return a dict
  """
  mydict = {}
  for parking, url in dict_url().items():
    mydict[parking] = xml_parse_url(url)
  return mydict
