import requests

# Amazonクラス
class Amazon(object):

	def	getrequest(self, amazon_url):
		my_header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; NP06; rv:11.0) like Gecko"
		}
		res = requests.get(amazon_url, headers = my_header)
		return res.text
