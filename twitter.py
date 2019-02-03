# Problem: want to collect text data using Twitter APIs

import numpy as np 
import json
import pandas as pd
import tweepy

# Credentials
consumer_key = "asdasdasda"
consumer_secret = "asdasdasd"
acess_token = "asdiashdasda"
acess_token_secret = "ahsdiuashdiuahs"

# Calling API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

