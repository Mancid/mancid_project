import configparser


def dict_url():
    url = configparser.ConfigParser()
    url.read('url.ini')
    all_url = list(url['url'])
    res = {}
    for simple_url in all_url:
        parking = simple_url.capitalize()
        link = url['url'][simple_url]
        res[parking] = link
    return res
