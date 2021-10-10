# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 19:13:31 2021

@author: Cecilia Battinelli
"""

import tweepy
import logging
from time import sleep
from config import create_api

"""
Parameters
    ----------
    api : Twitter API
        Twitter API based on the log in keys
    logger : RootLogger
        Logger to keep track of what it is done
    keyword: str
        The hashtag or word on which tweets are filtered
    num_items : int
        Number of tweets to process and possibly retweet and like
    user_name : str
        The authenticated user user name (@username)
"""
def retweet_and_like(api, logger, keyword, num_items, user_name):
  for tweet in tweepy.Cursor(api.search_30_day, label='dev', query=keyword).items(num_items):
      logger.info(f"Processing tweet id {tweet.id}")
      if tweet.user.screen_name == user_name:
        logger.info(f"The tweet is from myself.")
        continue
      if not tweet.retweeted:
        try:
          tweet.retweet()
          tweet.favorite()
          logger.info(f"The tweet is retweeted and liked.")
          sleep(10)
        except Exception:
          logger.error("Already retweeted.")


def main(keyword, num_items, user_name):
  # Initialize the API
  api = create_api()
  # Initialize the logger
  logging.basicConfig(level=logging.INFO)
  logger = logging.getLogger()

  retweet_and_like(api, logger, keyword, num_items, user_name)


if __name__ == "__main__":
    main('Roma', 5, 'cipbott')