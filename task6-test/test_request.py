# テストコード

# from api import *
from request import get_api,get_response_api,get_response_api_sub


#リクエスト関数のテスト
def test_get_api():
	test_keyword = "Pythonプログラミング入門"
	url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&keyword={}&applicationId=1017111620275786286"
	test_url = url.format(test_keyword)

	res = get_api(url=test_url)

	# テストコードの書き方
	# 正常処理
	assert len(res['Items']) >= 1
	assert res["Items"][0]["Item"]["itemCode"]

	# 異常処理
	test_keyword2 = "Pythonプログラミング入門あいうえおかきくけお"
	test2_url = url.format(test_keyword2)
	res = get_api(url=test2_url)
	# 見つからないため0件
	assert len(res['Items']) == 0

#レスポンス結果より上位階層の情報取得テスト
def test_get_response_api():

	#リクエスト実行
	test_keyword = "Pythonプログラミング入門"
	url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&keyword={}&applicationId=1017111620275786286"
	test_url = url.format(test_keyword)

	res = get_api(url=test_url)

	#正常系 
	test_dict = {'count':'検索結果数', 'page':'ページ', 'first':'ページ内商品始追番', 'last':'ページ内商品終追番', 'hits':'ヒット件数番', 'carrier':'キャリア情報', 'pageCount':'総ページ数'}
	#関数を使ってレスポンス情報取得
	test_result = get_response_api(res, test_dict)
	
	#テストコード
	assert len(test_result) == 7
	assert test_result[5][1] == 0 #0はPC,1はスマホ

	#異常系
	test2_dict = {'aaa':'検索結果数', 'bbb':'ページ'}
	#関数を使ってレスポンス情報取得
	test2_result = get_response_api(res, test2_dict)

	#テストコード
	#例外で[]が返ってくる
	assert test2_result == []

#レスポンス結果より上位階層の情報取得テスト
def test_get_response_api_sub():

	#リクエスト実行
	test_keyword = "Pythonプログラミング入門"
	url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&keyword={}&applicationId=1017111620275786286"
	test_url = url.format(test_keyword)

	test_res = get_api(url=test_url)

	#正常系
	test_dic_name = 'Item'
	test_dict = {'itemName':'商品名', 'itemPrice':'価格'}
	#関数を使ってレスポンス情報取得
	test_result = get_response_api_sub(test_res['Items'], test_dic_name, test_dict)
	
	#テストコード
	assert len(test_result[0]) == 2

	#異常系
	test2_dic_name = 'Product'
	test2_dict = {'aaa':'検索結果数', 'bbb':'ページ'}
	# #関数を使ってレスポンス情報取得
	test2_result = get_response_api_sub(test_res['Items'], test2_dic_name, test2_dict)

	# #テストコード
	# #例外で[]が返ってくる
	assert test2_result == []

