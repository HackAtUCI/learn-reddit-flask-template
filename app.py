from flask import Flask, render_template
import json
import reddit


app = Flask(__name__)

@app.route('/')
def index():
    #TODO: Assign a Reddit subreddit name to use in this function.
    subreddit_name = '' #Assign this variable to your favorite subreddit.
    #TODO: Create an instance of the praw Reddit object. Refer to reddit.py
    #TODO: Generate a list of top ten posts for your subreddit.
    #TODO: Pass the list you created above to the render_template function call below.
    return render_template('index.html',posts = ,name = )

if __name__ == "__main__":
    app.run(debug = True) #Set debug = False in a production environment