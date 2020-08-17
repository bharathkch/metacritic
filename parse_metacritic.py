#!/usr/local/python

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json


class Metacritic:
    """
    A simple class that takes a Metacritic URL and exposes method to return its titles and scores.
    """

    def __init__(self, url):
        """
        Constructor that takes the URL string and sets the instance variables for URL and result.
        :param url: string
        """
        self.url = url
        self.result = []

    def parse_metacritic(self):
        """
        Method that returns the titles and scores in JSON.
        :return: str
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

        return json.dumps(self.result)


if __name__ == '__main__':
    metacritic_obj = Metacritic("https://www.metacritic.com/game/playstation-4")
    print(metacritic_obj.parse_metacritic())
