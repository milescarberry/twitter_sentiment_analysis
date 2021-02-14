from textblob import TextBlob

import tweepy

import sys                # This module is part of the core Python stack.

import math               # This module is part of the core Python stack.

from dotenv import load_dotenv

from pathlib import Path

import os

env_path  = Path(".env")                    # env_path is an instance of the Path class.

load_dotenv(dotenv_path = env_path)

api_key = os.getenv("api_key")

api_secret_key = os.getenv("api_secret_key")

bearer_token = os.getenv("bearer_token")

access_token = os.getenv("access_token")

access_secret = os.getenv("access_secret")



# Now, let's create a twitter_api authentication handler.


auth_handler = tweepy.OAuthHandler(consumer_key = api_key, consumer_secret = api_secret_key)


auth_handler.set_access_token(access_token, access_secret)



api = tweepy.API(auth_handler)              # This is how we build the connection to the twitter_api.



search_term = "biden"


tweet_amount = 1000

polarity = 0

positive = 0

negative = 0

neutral = 0



# Now, let's create a "Cursor" object :-


cursor_object = tweepy.Cursor(api.search, q= search_term, lang = "eu")

tweets = cursor_object.items(tweet_amount)




for tweet in tweets:


    final_text = tweet.text.replace('RT', '')

    if final_text.startswith(" @"):

        position = final_text.index(":")

        if final_text[position+1] == ' ':

            final_text = final_text[position+2::1]

        else:

            final_text = final_text[position+1::1]



    else:

        if final_text.startswith("@"):


            position = final_text.index(" ")



            final_text = final_text[position+1::1]











    # So, we have "cleaned up" our messages/tweets.

    # Now, we will perform the "sentiment analysis" of our messages/tweets.

    # For performing the sentiment analysis, we need to create a "TextBlob" object.



    analysis = TextBlob(final_text)                   # We will be passing in our "cleaned up" tweet here as an argument.


    tweet_polarity = analysis.polarity


    if tweet_polarity < 15.00:

        negative+= 1

    elif tweet_polarity > 15.00:

        positive+= 1

    elif tweet_polarity == 0.00:

        neutral+= 1






    polarity = polarity + tweet_polarity









if polarity > 15.00:

    print()

    print("There is a positive trend.")

    print()

else:

    print()

    print("There is a negative trend.")

    print()




print("Polarity :- ", str(round(polarity, 2)))

print()

print("Positive Tweets :- ", positive)

print()

print("Negative Tweets :- ", negative)

print()

print("Neutral Tweets :- ", neutral)
