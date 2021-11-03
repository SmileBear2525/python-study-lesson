import tweet
import amazon

import signal
import time
import datetime
from bs4 import BeautifulSoup

from dotenv import load_dotenv
load_dotenv()

import os
AMAZON_URL = os.getenv('AMAZON_URL')

#在庫フラグ(0:在庫なし,1:在庫あり)
stock_flg = 0

def check_stock(arg1, arg2):
	print('関数:check_stock')
	# 現在時間の表示
	dt = datetime.datetime.now()
	print(dt)
	
	#グローバル変数宣言
	global stock_flg

	# 在庫の確認
	print(f'在庫：{stock_flg}')

	#Amazon在庫チェック
	am = amazon.Amazon()
	data_amazon = am.getrequest(AMAZON_URL)
	#print(data_amazon)
	soup = BeautifulSoup(data_amazon, 'html.parser')
	#print(soup)
	detail = soup.find(id="add-to-cart-button")
	# idが見つからない場合、Noneが返ってくる
	post_msg = ''
	if detail == None:
		post_msg = f'在庫がなくなりました {dt}'
	else:
		post_msg = f'在庫があるので、ツイートします {dt}'

	# ツイート投稿
	if((stock_flg == 1 and detail == None) or (stock_flg == 0 and detail != None)):
		tw = tweet.Tweet()
		api = tw.api()
		tw.msg_post(api, post_msg)
	else:
		print('変化なしのためツイートしません')

	# 在庫フラグの変更
	if detail == None:
		stock_flg = 0
	else:
		stock_flg = 1


def main():
	#タイマーの強制終了はCTRL+C

	# signalを使ってcheck_stock関数の呼び出し
	signal.signal(signal.SIGALRM, check_stock)
	signal.setitimer(signal.ITIMER_REAL, 0.1, 10) #15秒おきに実行
	
	while True:
		print('timesleep')
		time.sleep(10) #15秒毎


if __name__ == "__main__":
	main()