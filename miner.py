import tweepy
import json
import re
from tweepy import OAuthHandler

# Consumer keys and access tokens, used for OAuth
consumer_key = 'hxe6RcxfQ2wFMXlmNRzcYlQlB'
consumer_secret = '3lNHyj3kPJi0V0KU88VwfjIzT72i6CWLJAUe1pZpeRfA5XseKO'
access_token = '269242039-i0kPdHsgxLs90SKt15jiobQu81J7yThMG8r2NlMz'
access_token_secret = 'AThceWaEz2HchARZ4n5QjP0ocudWongKME2YzZbFE3inh'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Mines as many tweets from Donald Trump's Twitter as possible, which given the sheer frequency is only about a year's worth
for status in tweepy.Cursor(api.user_timeline, screen_name='@realDonaldTrump', tweet_mode='extended').items():
    if status.full_text.find('RT @') == -1:
        #status.text = re.sub("http\S+", "", status.text)
        print(json.dumps(status._json))
