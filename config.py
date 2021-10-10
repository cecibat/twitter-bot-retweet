# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 18:59:02 2021

@author: Cecilia Battinelli
"""

import tweepy

def create_api():
  CONSUMER_KEY = ''
  CONSUMER_SECRET = ''
  ACCESS_KEY = ''
  ACCESS_SECRET = ''
  
  auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
  api = tweepy.API(auth)
  return api

