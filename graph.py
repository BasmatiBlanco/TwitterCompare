import matplotlib.pyplot as plt
import tweepy
from tweepy import OAuthHandler
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
x = []
y = []
x2 = []
y2 = []
tweet_fav1 = 0
tweet_fav2 = 0

print ("Choose your first user to compare")
first = input()
print ("Choose your second under to compare")
second = input()
print("Do you want to see a graph(Y/N)")
graph_choice = input()
if graph_choice != 'Y' and graph_choice != 'y' and graph_choice != 'N'and graph_choice != 'n':
    graph_choice = input("Please enter Y or N")


def compare_tweets_graph(screen_name, graph_order):
    recent_tweets = api.user_timeline (screen_name = screen_name,count=200)
    tweet_list = []
    tweet_list.extend(recent_tweets)

    marker = tweet_list[-1].id-1
    while len(recent_tweets) > 0:
        recent_tweets = api.user_timeline (screen_name = screen_name,count=200, max_id=marker)
        tweet_list.extend(recent_tweets)
        marker = tweet_list[-1].id-1  
        if graph_order == 1:   
            for tweet in tweet_list:
                if tweet.text.startswith("RT"):
                    tweet_list.remove(tweet)
                else:
                    y.append(tweet.favorite_count)
                    x.append(tweet.created_at)
        elif graph_order == 2:
            for tweet in tweet_list:
                if tweet.text.startswith("RT"):
                    tweet_list.remove(tweet)
                else:
                    y2.append(tweet.favorite_count)
                    x2.append(tweet.created_at)
  
def graph_tweets(user1, user2):
    compare_tweets_graph(user1, 1)
    compare_tweets_graph(user2, 2)
    plt.plot(x, y, label = user1 + str(tweet_fav1))
    plt.plot(x2, y2, label = user2 + str(tweet_fav2))  
    plt.xlabel("Time") 
    plt.ylabel('Faves') 
    plt.title("Faves over Time ") 
    plt.legend()
    plt.show()

def recent_tweet_list(screen_name):
    recent_tweets = api.user_timeline (screen_name = screen_name,count=200)
    tweet_list = []
    tweet_list.extend(recent_tweets)
    marker = tweet_list[-1].id-1
    while len(recent_tweets) > 0:
        recent_tweets = api.user_timeline (screen_name = screen_name,count=200, max_id=marker)
        tweet_list.extend(recent_tweets)
        marker = tweet_list[-1].id-1       
    tweet_fav = 0
    for tweet in tweet_list:
        if tweet.text.startswith("RT"):
            tweet_list.remove(tweet)
        else:
            tweet_fav += tweet.favorite_count
    return tweet_fav

def compare_tweet_favs(user1, user2):
    total_user1= recent_tweet_list(user1)
    total_user2= recent_tweet_list(user2)
    if total_user1 > total_user2:
        print( str(user1) + " is the winner with " + str(total_user1) + " favorites compared to " + str(user2) + "'s " + str(total_user2) + " favorites")
    elif total_user1 < total_user2:
        print( str(user2) + " is the winner with " + str(total_user2) + " favorites compared to " + str(user1) + "'s " + str(total_user1) + " favorites")
    elif total_user1 == total_user2:
        print("It's a tie! both " + str(user1) + " and " + str(user2) + " have the same amount of favorites")

if graph_choice == 'y' or graph_choice == 'Y':
    graph_tweets(first, second)
elif graph_choice == 'n' or graph_choice == 'N':   
    compare_tweet_favs(first, second)