import tweepy
import os

auth = tweepy.OAuthHandler('LbUo13xcIfdIYvoEHCEgL921K', 'GVReG2W4mM0ehxVHzqR0HWZ8T52QXWBLXAou9PR1Blf8Dn821c')
auth.set_access_token ('92941839-FN3Z38BYlE9kYdqTaGEJXrTMjtgrkUcHk6JBqkyrA', 'XdbWbtcLiZiHTCVaYrax53fcOOgqUjC7rIMumkZe410k2')

twitter_api = tweepy.API(auth)

legaltech_tweets = twitter_api.search(q="#LegalTech") #twitter handle searched for

from flask import Flask, render_template
app = Flask("demoApp")

@app.route("/")
def index():
	return render_template("index.html", tweets=legaltech_tweets)


if 'PORT' in os.environ:
	# app running on Heroku
	app.run(host="0.0.0.0", port=int(os.environ["PORT"]))
else:
	# app running locally (i.e you can see it by typing 'localhost:5000' in browser)
	app.run(debug=True)