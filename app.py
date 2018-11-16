from flask import Flask, render_template
import json
import reddit


app = Flask(__name__)

@app.route('/')
def index():
    #TODO: (13) Assign a Reddit subreddit name to use in this function.
    subreddit_name = '' #Assign this variable to your favorite subreddit.
    #TODO: (14) Create an instance of the praw Reddit object. Refer to reddit.py
    #TODO: (15) Generate a list of top ten posts for your subreddit.
    #TODO: (16) Pass the list you created above to the render_template function call below.
    return render_template('index.html',posts = ,name = )

if __name__ == "__main__":
    app.run(debug = True) #Set debug = False in a production environment