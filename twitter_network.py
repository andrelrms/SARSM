from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import tweepy
import csv 
##import networkx as nx
##import matplotlib.pyplot as plt
##import re
##import numpy as np
##import pandas as pd

# some references  from where this code is based of
#https://thebrickinthesky.wordpress.com/2014/06/26/maths-with-python-6-twitter-api-tweepy-for-social-media-and-networks-with-gephi/
#http://nealcaren.web.unc.edu/an-introduction-to-text-analysis-with-python-part-2/

## Insert your consumer and acess token
consumer_key=""
consumer_secret=""

access_token=""
access_token_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

### Getting followers and saving output into csv file
# insert user which you would like to build your network
user='' 
print(user)
#This creates a csv file and defines that each new entry will be in a new line 
csvfile=open(user+'netnew2212_2.csv', 'wb') 
spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL) 
#This is the function that takes a node (user) and looks for all its followers #and print them into a CSV file... and look for the followers of each follower... 
'''
#original function
def fib(n,user,spamwriter):
    print(n)
    if n>0:
        #There is a limit to the traffic you can have with the API, so you need to wait 
        #a few seconds per call or after a few calls it will restrict your traffic 
        #for 15 minutes. This parameter can be tweeked 
        time.sleep(40)
        try:
            users=api.followers(user)
            for follower in users:
                spamwriter.writerow([user+';'+follower.screen_name]) 
                fib(n-1,follower.screen_name,spamwriter)
            #n defines the level of autorecurrence
        except tweepy.TweepError:
            print("Error")
'''


# only get users with a maximum numbre o followers 
# fib3 has the problem that is has too many time.sleep so it becomes very slow
def fib3(n,user,spamwriter,maxfol):
    print(n)
    
    if n>0:
        #There is a limit to the traffic you can have with the API, so you need to wait 
        #a few seconds per call or after a few calls it will restrict your traffic 
        #for 15 minutes. This parameter can be tweeked 
        time.sleep(20)
        try:
            #users= tweepy.Cursor(api.followers, screen_name=user).items()
            for follower in tweepy.Cursor(api.followers, screen_name=user).items():
                print("Getting number of followers")
                usert =  api.get_user(follower.screen_name)
                usernfo = usert.followers_count
                print(follower.screen_name+': '+str(usernfo))
                time.sleep(20)
                if usernfo<maxfol:
                    print("Number of followers OK")
                    print(user+';'+follower.screen_name)
                    spamwriter.writerow([user+';'+follower.screen_name])
                    fib3(n-1,follower.screen_name,spamwriter,maxfol)
                    time.sleep(20)
                else:
                    print("Number of follower too high")
                    time.sleep(20)
        #n defines the level of autorecurrence
        except tweepy.TweepError as e:
            print("Error")
            print(e)
            time.sleep(900) # sleeps for 15 minutes in case it exceeds rate limit
            pass 




# only get users with a maximum numbre o followers
# same as fib3 but only sleeps when it reaches twitter maximum rate allowed
def fib4(n,user,spamwriter,maxfol):
    print(n)
    
    if n>0:
        #time.sleep(20)
            #users= tweepy.Cursor(api.followers, screen_name=user).items()
        for follower in tweepy.Cursor(api.followers, screen_name=user).items():
            try:
                print("Getting number of followers")
                usert =  api.get_user(follower.screen_name)
                usernfo = usert.followers_count
                print(follower.screen_name+': '+str(usernfo))
                #time.sleep(20)
                if usernfo<maxfol:
                    print("Number of followers OK")
                    print(user+';'+follower.screen_name)
                    spamwriter.writerow([user+';'+follower.screen_name])
                    fib4(n-1,follower.screen_name,spamwriter,maxfol)

                
                else:
                    print("Number of follower too high")
            except tweepy.TweepError as e:
                print("Error")
                print(e)
                time.sleep(900) # sleeps for 15 minutes in case it exceeds rate limit
        
        
           





n=2 # defines the level of autorecurrence
fib4(n,user,spamwriter,300) 


