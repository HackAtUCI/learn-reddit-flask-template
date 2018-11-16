import praw #This module is used to create Reddit instances
import json
from urllib import request

'''The reddit_instance object will contain the reddit instance we will create to handle all API calls. 
   Read the Python Reddit API Wrapper(PRAW) documentation for further details'''

#TODO: (1) Create a Reddit app at https://reddit.com/prefs/apps
#TODO: (2) Update your credentials in the credentials_template.json file
#TODO: (3) Rename credentials_template.json to credentials.json
#Tip: bash command for above step: cp credentials_template.json credentials.json

def create_reddit_instance(read_only = False):
    '''This function reads the crendentials from credentials.json and creates a Reddit instance.
        You will use this instance to retrieve further information. Before you complete this 
        function, be sure to create your credentials on the Reddit website, update 
        credentials_template.json and rename it to credentials.json
    '''
    credentials = None
    #TODO: (4) Open 'credentials.json' and read the information into the credentials object initialized above. 
    
    '''The read only parameter determines whether a read-only object,i.e, no login required, 
    or an OAuth2 authenticated object should be created
    '''
    #TODO: (5) Pass all parameters relevant to read-only and user-authenticated objects. One of the parameters is already completed for you.
    if(not read_only):
        reddit_instance = praw.Reddit(client_id = credentials['client_id'],)
    else:
        reddit_instance = praw.Reddit()
    #TODO: (6) Return the reddit instance you created below.
    return 
    
    
def ten_top_posts(reddit_instance, subreddit_name):
    '''This function takes a subreddit name as a string and prints out ten posts
    under the top category'''
    #TODO: Create a subreddit instance with subreddit_name and reddit_instance.

    #TODO: (7) Return the top posts in the subreddit by calling the .top() function on it.
    #TODO: (8) Set the limit parameter for the top function to 10, so that the top 10 posts are returned.
    return 

if __name__ == '__main__':
    '''Experiment with your reddit function here. Examine the output on the console.'''
    #TODO: (9) Set the value of subreddit_name to your favorite subreddit.
    subreddit_name = '' 
    #TODO: (10) Create a new instance of the praw Reddit object.

    #TODO: (11) Generate a list of top ten posts for your subreddit, using the praw Reddit object you created.

    #TODO: (12) Iterate through the posts list returned by the function call above, and print its title attribute
    for():
        pass


    


    