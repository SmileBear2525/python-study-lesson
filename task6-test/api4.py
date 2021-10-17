import request as req
import requests
import time
import pandas

#課題４
#ランキング取得CSV化
#ジャンルID取得↓
#https://nokin-taro.com/apiidpython/

#APIよりジャンルIDの調査
base_url = 'https://app.rakuten.co.jp/services/api/IchibaGenre/Search/20140222'
item_parameters = {
  'applicationId':'1017111620275786286',
  'format':'json',
  'formatVersion':2,
  'genreId':0,
}

#最上位階層の取得
r = requests.get(base_url, params=item_parameters)
item_data = r.json()
time.sleep(1) #楽天API規約に則って1secあける

#階層を掘ってジャンル情報を取得
for i in item_data["children"]:
	# 最上段ジャンル情報
	parent_g_id = i["genreId"]
	parent_g_name = i["genreName"]
	print(f"{parent_g_id}：{parent_g_name}")

#------------------
#APIよりランキングの取得
rankList_csv = []

#ジャンルID 551167：スイーツ・お菓子を使用
rank_url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?format=json&applicationId=1017111620275786286&genreId=551167'

#リクエスト実行
response_rank = req.get_api(rank_url)

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
df.to_csv('result.csv')