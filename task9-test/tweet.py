import tweepy
# from dotenv import load_dotenv
# load_dotenv()

import os
# API_KEY = os.getenv('API_KEY')
# API_SECRET = os.getenv('API_SECRET')
# ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
# ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# tweeクラス
class Tweet:
	API_KEY = ''
	API_SECRET = ''
	ACCESS_TOKEN = ''
	ACCESS_TOKEN_SECRET = ''

	def __init__(self):
		self.API_KEY = os.getenv('API_KEY')
		self.API_SECRET = os.getenv('API_SECRET')
		self.ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
		self.ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
	
	# API取得
	def api(self):
		auth = tweepy.OAuthHandler(self.API_KEY, self.API_SECRET)
		auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)
		return tweepy.API(auth)

	# ツイートを投稿
	def msg_post(self, api, msg):
		print(msg)
		api.update_status(msg)
		print('ツイートしました')
