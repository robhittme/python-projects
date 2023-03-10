from termcolor import colored, cprint
from configparser import ConfigParser 
import requests
import json
from sys import argv

config = ConfigParser()
config.read('config.ini')

API_KEY = config['news']['NewsApiKey'] 
url = ('https://newsapi.org/v2/top-headlines?')
response = requests.get(url)

def get_us_headlines():
    query_parameters = {
            "country": "us",
            "apiKey": API_KEY
     }
    return _get_articles(query_parameters)

def get_articles_by_category(category):
    query_parameters = {
            "category": category,
            "country": "us",
            "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def _get_articles(params):
    response = requests.get(url,params=params)
    articles = response.json()['articles']

    for article in articles:
        if article['description'] == None:
            continue
        cprint(colored(article['title'], 'green', attrs=["bold"]))
        print(colored(article['description'], 'white'))
        print(colored(article['url'], 'light_grey'))
        print(colored(article['source']['name'], 'magenta'))
        print('_____')



def json_formatter(js):
    return json.dumps(js, indent=2)

if __name__ == "__main__":
    print(f"Getting news for {argv[1]}...\n")
    if argv[1]:
        get_articles_by_category(argv[1])
    else:
        get_us_headlines()
