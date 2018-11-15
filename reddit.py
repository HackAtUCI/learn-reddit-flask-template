import praw #This module is used to create Reddit instances
import json
from urllib import request

'''The reddit_instance object will contain the reddit instance we will create to handle all API calls. 
   Read the Python Reddit API Wrapper(PRAW) documentation for further details'''


def create_reddit_instance(read_only = False):
    '''This function reads the crendentials from credentials.json and creates a Reddit instance.
        You will use this instance to retrieve further information. Before you complete this 
        function, make sure to create your crendentials on the Reddit website, update 
        credentials_template.json and rename it to credentials.json
    '''
    credentials = None
    #TODO: Open 'credentials.json' and read the information into the credentials object initialized above. 
    
    '''The read only parameter determines whether a read-only object,i.e, no login required, 
    or an OAuth2 authenticated object should be created
    '''
    #TODO: Pass all parameters relevant to read-only and user-authenticated objects. One of the parameters is already completed for you.
    if(not read_only):
        reddit_instance = praw.Reddit(client_id = credentials['client_id'],)
    else:
        reddit_instance = praw.Reddit()
    #TODO: Return the reddit instance you created below.
    return 
    
    
def ten_top_posts(reddit_instance, subreddit_name):
    '''This function takes a subreddit name as a string and prints out the ten latest posts
    under the hot category'''
    #TODO: Create a subreddit instance with subreddit_name and reddit_instance.

    #TODO: Return the top posts in the subreddit by calling the .top() function on it.
    #TODO: Set the limit parameter for the top function to 10, so that the top 10 posts are returned.
    return 

if __name__ == '__main__':
    '''Experiment with your reddit function here. Examine the output on the console.'''
    #TODO: Set the value of subreddit_name to your favorite subreddit.
    subreddit_name = '' 
    #TODO: Create a new instance of the praw Reddit object.

    #TODO: Generate a list of top ten posts for your subreddit, using the praw Reddit object you created.

    #TODO: Iterate through the posts list returned by the function call above, and print its title attribute
    for():
        pass


    


    