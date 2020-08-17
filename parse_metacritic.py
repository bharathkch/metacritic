#!/usr/local/python

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json
import os

from flask import Flask
from dotenv import load_dotenv
from my_logger import my_logger



# loading env variables before app start up
# env vars can be accessed from os.environ dict
CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config')
load_dotenv(os.path.join(CONFIG_PATH, '.env'))
print(os.path.join(CONFIG_PATH, '.env'))


# Configures  logging
logger = my_logger()


# Initiates Flask app
application = Flask(__name__)

# passes the environment variables to Flask app
application.config.update(os.environ)


class Metacritic:
    """
    A simple class that takes a Metacritic URL and exposes method to return its titles and scores.
    """

    def __init__(self, url):
        """
        Constructor that takes the URL string and sets the instance variables for URL and result.
        :param url: none
        """
        self.url = url
        self.result = []

    def parse_metacritic(self):
        """
        Method that returns the titles and scores in JSON.
        :return: None
        """
        req = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        web_page = urlopen(req).read()

        soup = BeautifulSoup(web_page, "html.parser")

        containers = soup.find_all("tr", {"class": "score_title_row"})

        for each_container in containers:
            this_title = each_container.find("a", {"class": "product_title"}).string.strip()
            this_score = each_container.find("span", {"class": "metascore_w"}).string.strip()

            this_element = {"title": this_title, "score": this_score}

            self.result.append(this_element)

            logger.debug(f"found {len(self.result)} games")


    def to_json(self, inp=None):
        """
        Converts the result object to JSON
        TODO:
        - Beautify JSON
        :return: str
        """

        return json.dumps(inp)


@application.route('/ping')
def ping():
    """
    A ping function  for health checks.
    :return: str
    """
    return "OK"

@application.route('/games', methods=['GET'])
def fetch_top_games():
    """
    Returns the games in JSON format.
    :return: list of games in JSON
    """

    logger.debug("retrieving the games from a predefined metacritic URL")
    metacritic_obj = Metacritic(application.config['mc_url'])
    metacritic_obj.parse_metacritic()
    return(metacritic_obj.to_json(metacritic_obj.result))

@application.route('/games/<game_title>', methods=['GET'])
def fetch_game(game_title):
    """
    Fetches a particular game from the parsed metacritic page.
    :param game_title: str
    :return: JSON with "title and score" or a custom error message
    """

    metacritic_obj = Metacritic(application.config['mc_url'])
    metacritic_obj.parse_metacritic()

    title_found = False
    for each_game in metacritic_obj.result:
        if each_game['title'] == game_title:
            title_found = True
            response = each_game

    if title_found:
        return(metacritic_obj.to_json(response))
    else:
        return(metacritic_obj.to_json({"Error": f"A game with title  '{game_title}' Not found"}))


if __name__ == '__main__':
    application.run(host=application.config['flask_hostname'], port=application.config['flask_port'], debug=False)
