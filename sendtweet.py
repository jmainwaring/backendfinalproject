import tweepy 

def send_tweet():
  
	# Adding necesssary keys
	consumer_key ="9B4yWmBWEo3wa2iZ3NoSvwUgF"
	consumer_secret ="JPqH0f17IraRvrtLn1HGSSqnU9NruVbp2dCtoy60FvBySPySeQ"
	access_token ="1121820237500829696-g4R2e8gpkWIL6FsHK97mgHtZploKDK"
	access_token_secret ="B4bVJSEtcPyGGV9ierSqzLMA53mymYbVytRBgmlJ0qqMx"
	  
	# Authenticating consumer key and secret 
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
	  
	# Authenticating access token and secret
	auth.set_access_token(access_token, access_token_secret) 
	api = tweepy.API(auth) 
	  
	# Posting the tweet
	api.update_status(status="Just completed a SQL Practice problem")



send_tweet()