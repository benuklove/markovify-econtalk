import tweepy
import markovify

from twitter_credentials import consumer_key, consumer_secret,\
    access_token, access_token_secret


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# api.update_status("Hello, world! EconTalk Markov chain fun with Python and tweepy forthcoming!")

with open("data/corpus.txt") as corpus_file:
    corpus = corpus_file.read()

model = markovify.Text(corpus)

# print(model.make_short_sentence(140))


class TweetBot:
    def __init__(self, corpus):
        # load corpus & build model
        self.load_corpus(corpus)

        # initialize Twitter authorization with Tweepy
        pass

    def load_corpus(self, corpus):
        # open our corpus & run it through Markovify
        pass

    def tweet(self):
        # generate Markov tweet & send it
        pass

    def automate(self, delay):
        # automatically tweet every delay seconds
        pass
