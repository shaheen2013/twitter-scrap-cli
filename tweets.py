# importing libraries and packages
import snscrape.modules.twitter as sntwitter
import pandas as pd
import os, time
from progressbar import printProgressBar

# Creating list to append tweet data 
tweets = []
followers = []
followings = []


def getTweets(username, number_of_tweets):
    """ 
    If file exists then remove the file, and make new file
    """
    prefix = str(time.monotonic_ns())
    if os.path.exists(prefix + '-tweets.xlsx'):
        os.unlink(prefix + "-tweets.xlsx")
    
    # Using TwitterSearchScraper to scrape data and append tweets to list
    username = f'from:{username}'
    # Initial call to print 0% progress
    # A List of Items
    items = list(range(0, number_of_tweets))
    l = len(items)
    printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(username).get_items()): #declare a username 
        time.sleep(0.1)
        if i >= number_of_tweets: #number of tweets you want to scrape
            break
        tweets.append({ 'URL' : tweet.id,  'Text': tweet.content, 'UTC' : pd.to_datetime(tweet.date).to_datetime64() }) #declare the attributes to be returned
        printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
        
    tweets_data = pd.DataFrame(tweets)
    followers_data = pd.DataFrame(followers)
    followings_data = pd.DataFrame(followings)

    # Generate Excel file with defferet sheet

    with pd.ExcelWriter(prefix + '-tweets.xlsx') as writer:  
        tweets_data.to_excel(writer, sheet_name='Tweets')
        followers_data.to_excel(writer, sheet_name='Followers')
        followings_data.to_excel(writer, sheet_name='Followings')
        


        





if __name__ == "__main__":
    
    print(""" 
        #######################################################################
        #####     Please Enter you twitter username  ##########################
        #######################################################################
        """)
    username = str(input("Write your username: ") or 'POTUS')
    number_of_tweets = int(input('How many tweets you want? : ') or 1)
    print(f'Please wait... Collect tweets... Your username is {username}')
    getTweets(username, number_of_tweets)
