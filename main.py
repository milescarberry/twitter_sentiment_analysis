from textblob import TextBlob

import tweepy

import sys                # This module is part of the core Python stack.

from dotenv import load_dotenv



with open(".env") as env_file:

    api_key, api_secret_key, bearer_token = load_dotenv(env_file, Verbose = True)
