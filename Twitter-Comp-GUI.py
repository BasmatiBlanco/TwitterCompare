import tkinter as tk
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
    plt.plot(x, y, label = user1)
    plt.plot(x2, y2, label = user2)  
    plt.xlabel("Time") 
    plt.ylabel('Faves') 
    plt.title("Faves over Time ") 
    plt.legend()
    plt.show()

root = tk.Tk()

greeting = tk.Label (
    text = "Compare Users", 
    foreground = "black",
    )
first_user = tk.Label (
    text = "First", 
    foreground = "black",
    )
second_user =  tk.Label (
    text = "Second", 
    foreground = "black",
    )
entry_first = tk.Entry(fg = "black", bg = "AntiqueWhite1", width = 50)
entry_second = tk.Entry(fg = "black", bg = "AntiqueWhite1", width = 50)

button = tk.Button(
    text="Submit",
    width=25,
    height=1,
    bg="black",
    fg="white",
    command = lambda: get_in_graph()
    )

def get_in_graph():
    first_in = entry_first.get()
    second_in = entry_second.get()
    graph_tweets(first_in, second_in)

greeting.pack()
first_user.pack()
entry_first.pack()
second_user.pack()
entry_second.pack()
button.pack()
root.mainloop()