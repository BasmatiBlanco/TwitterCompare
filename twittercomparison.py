import tweepy
from tweepy import OAuthHandler
from credentials import *
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

tweet_list= []


def recent_tweet_list(screen_name):
    new_tweets = api.user_timeline (screen_name = screen_name,count=200)
    tweet_list.extend(new_tweets)
    total = 0
    for tweet in tweet_list:
        if tweet.text.startswith("RT"):
            tweet_list.remove(tweet)
        elif tweet.text.startswith("@"):
            tweet_list.remove(tweet)
        else:
            total += int(tweet.favorite_count)
        return int(total)

def compare_tweet_favs(user1, user2):
    total_user1= recent_tweet_list(user1)
    total_user2= recent_tweet_list(user2)
    if total_user1 > total_user2:
        print( str(user1) + " is the winner with " + str(total_user1) + "favorites")
    elif total_user1 < total_user2:
        print( str(user2) + " is the winner with " + str(total_user2) + "favorites")
    elif total_user1 == total_user2:
        print("It's a tie! both " + str(user1) + " and " + str(user2) + " have the same amount of favorites")



compare_tweet_favs("RealDonaldTrump", "chrissyteigen")