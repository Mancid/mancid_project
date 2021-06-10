import configparser
import logging


def dict_url(conf):
  """Add all url from file url.ini with
  key = name of the parking end value is
  the url.

  :returns: dictionnary with all parking and url
  :rtype: dict
  """
  url = configparser.ConfigParser()
  logging.debug("initializing the variable url")
  url.read(conf)
  logging.debug("read the file")
  logging.debug("all url in file %s", list(url["url"]))
  res = {}
  for simple_url in list(url["url"]):
    parking = simple_url.capitalize()
    link = url["url"][simple_url]
    res[parking] = link
  logging.info("this is the dict with keys and urls %s", res)
  return res
