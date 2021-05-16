import configparser
import logging


def dict_url():
  """
  This function return a dict with
  keys = the name of the park , and the values
  is the url. We need to recover url for download
  the xml
  """
  url = configparser.ConfigParser()
  logging.debug("initializing the variable url")
  url.read('url.ini')
  logging.debug("read the file")
  logging.debug("all url in file %s", list(url['url']))
  res = {}
  for simple_url in list(url['url']):
    parking = simple_url.capitalize()
    link = url['url'][simple_url]
    res[parking] = link
  logging.info("this is the dict with keys and urls %s", res)
  return res
