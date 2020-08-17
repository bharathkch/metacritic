#!/usr/local/python

import pytest
from parse_metacritic import Metacritic
from my_logger import my_logger


# Configures  logging
logger = my_logger()

#TODO: setup and teardown to promote DRYness?
#TODO: More test cases

@pytest.mark.parametrize("test_url, min_length" ,[("https://www.metacritic.com/game/playstation-4", 1),
                                                      ("http://google.com", 0)])
def test_parse_metacritic(test_url, min_length):
    """
    A function that takes a URL as in input and performs tests against parse_metacritic function.
    :param test_url: URl
    :param min_length: int
    :return: None
    """

    test_obj = Metacritic(test_url)
    logger.info(f"parsing the contents from {test_url} \n")

    _ = test_obj.parse_metacritic()
    resp_length = len(test_obj.result)
    assert resp_length >= min_length


@pytest.mark.parametrize("test_url, test_input, expected_type",
                         [("https://www.metacritic.com/game/playstation-4", {"foo": "bar"}, str)])
def test_to_json(test_url, test_input, expected_type):
    """
    Test cases for to_json function.
    :param test_url: URL for the Metacritic constructor
    :param test_input: dict
    :param expected_type: data-type
    :return: None
    """

    test_obj = Metacritic(test_url)

    logger.info(f"executing test for {test_input} \n")
    res = test_obj.to_json(test_input)

    assert type(res) == expected_type
