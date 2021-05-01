import configparser
import urllib.request
import shutil


def config():
    url = configparser.ConfigParser()
    url.read('url.ini')
    return url, list(url['url'])


def download():
    url, all_url = config()
    for simple_url in all_url:
        parking = simple_url.capitalize()+'.xml'
        link = url['url'][simple_url]
        urllib.request.urlretrieve(link, parking)
        shutil.move(parking, f'./liens/{parking}')
