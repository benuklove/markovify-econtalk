"""
    Twitter bot to share 140 character markov chains from
    EconTalk podcast transcripts.

"""

import tweepy
import markovify

from twitter_credentials import *
from time import sleep


def main():
    bot = TweetBot("data/corpus.txt")
    bot.automate(3600)


class TweetBot:
    def __init__(self, corpus):
        # load corpus & build model
        self.load_corpus(corpus)

        # initialize Twitter authorization with Tweepy
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def load_corpus(self, corpus):
        # open our corpus & run it through Markovify
        with open(corpus) as corpus_file:
            corpus_lines = corpus_file.read()
        self.model = markovify.Text(corpus_lines)

    def tweet(self):
        # generate Markov tweet & send it
        message = self.model.make_short_sentence(140)
        try:
            self.api.update_status(message)
        except tweepy.TweepError as error:
            print(error.reason)

    def automate(self, delay):
        # automatically tweet every delay seconds
        while True:
            self.tweet()
            sleep(delay)


if __name__ == '__main__':
    main()
