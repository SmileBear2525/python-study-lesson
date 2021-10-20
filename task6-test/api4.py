import request as req
import requests
import time
import pandas

RAKUTEN_API_ICHIBAGENRE = "https://app.rakuten.co.jp/services/api/IchibaGenre/Search/20140222"
APPLICATION_ID = "1017111620275786286"

#APIよりジャンルIDの調査
def search_genre():

	#ジャンルID取得↓
	#参考URL:https://nokin-taro.com/apiidpython/

	#APIよりジャンルIDの調査
	item_parameters = {
		'applicationId':APPLICATION_ID,
		'format':'json',
		'formatVersion':2,
		'genreId':0,
	}

	#最上位階層の取得
	item_data = req.get_api_param(RAKUTEN_API_ICHIBAGENRE, item_parameters)
	time.sleep(1) #楽天API規約に則って1secあける

	#階層を掘ってジャンル情報を取得
	for i in item_data["children"]:
		# 最上段ジャンル情報
		parent_g_id = i["genreId"]
		parent_g_name = i["genreName"]
		print(f"{parent_g_id}：{parent_g_name}")

RAKUTEN_API_PRODUCT = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628"



def rankingList_to_csv(genre_id: str):
	#課題４
	#ランキング取得CSV化

	#APIよりランキングの取得
	#リクエスト
	params = {
		"format": "jason",
		"applicationId": APPLICATION_ID,
		"genreId" : genre_id
	}

	#リクエスト実行
	response_rank = req.get_api_param(RAKUTEN_API_PRODUCT, params)

	#レスポンス結果より取得する要素のセット
	dict = {'title':'タイトル', 'lastBuildDate':'更新日'}

	#関数を使ってレスポンス情報取得
	result = req.get_response_api(response_rank, dict)

	#リクエスト結果をリスト化する関数呼び出し
	dic_element_name = 'Item'
	#CSV出力するカラム
	output_dict = {'rank':'ランク', 'itemName':'商品名', 'itemPrice':'価格', 'catchcopy':'キャッチコピー', 'itemUrl':'商品URL', 'shopName':'ショップ名'}

	#関数を使ってレスポンス情報のサブ階層取得
	result = req.get_response_api_sub(response_rank['Items'], dic_element_name, output_dict)
	# print(result)

	#CSV書き込み
	output_param = []
	for key,value in output_dict.items():
		output_param.append(value)
	# print(output_param)

	df = pandas.DataFrame(result, columns=output_param)
	output_file = "result.csv"
	df.to_csv(output_file)
	print(f"CSV出力完了 ファイル名：{output_file}")

	#戻り値 List（ランク、商品名、価格、キャッチコピー、商品URL、ショップ名)
	return result

if __name__ == "__main__":
	# ジャンルIDの調査
	search_genre()

	#ジャンルID 551167：「スイーツ・お菓子」を使用
	genreId="551167"
	rankingList_to_csv(genreId)

