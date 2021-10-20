import request as req

RAKUTEN_API_ICHIBAITEM = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
APPLICATION_ID = "1017111620275786286"

def search_items(keyword: str):
	#課題２
	#リクエスト
	#APIよりキーワードをキーに商品取得
	params = {
		"format": "jason",
		"applicationId": APPLICATION_ID,
		"keyword" : keyword
	}

	#リクエスト実行
	response = req.get_api_param(RAKUTEN_API_ICHIBAITEM, params)

	#レスポンス結果より取得する要素のセット
	dict = {'count':'検索結果数', 'page':'ページ', 'first':'ページ内商品始追番', 'last':'ページ内商品終追番', 'hits':'ヒット件数番', 'carrier':'キャリア情報', 'pageCount':'総ページ数'}

	#関数を使ってレスポンス情報取得
	result = req.get_response_api(response, dict)
	# print(result)
	for key, value in result:
		print(f"{key}：{value}")

	#リクエスト結果取得
	# print(f"検索結果数：{response['count']}")
	# print(f"ページ：{response['page']}")
	# print(f"ページ内商品始追番：{response['first']}")
	# print(f"ページ内商品終追番：{response['last']}")
	# print(f"ヒット件数番：{response['hits']}")
	# print(f"キャリア情報：{response['carrier']}")
	# print(f"総ページ数：{response['pageCount']}")

	pageCount = response['pageCount']
	pageCnt = int(pageCount)

	counter = 0
	itemList = []

	#リクエスト結果-商品取得、リスト化
	#ページ分ループ
	#リクエスト結果１ページに30件しか取得できないため、ページパラメータに持たせてリクエストする
	for page in range(pageCnt):
		#print(f"========={page+1}ページ目=========")
		
		#ページ毎リクエスト
		params_page = {
			"format": "jason",
			"applicationId": APPLICATION_ID,
			"keyword" : keyword,
			"page": page+1
		}
		
		res_page = req.get_api_param(RAKUTEN_API_ICHIBAITEM, params_page)

		dic_element_name = 'Item'
		dict_item_sub = {'itemName':'商品名', 'itemPrice':'価格'}

		#関数を使ってレスポンス情報のサブ階層取得
		result = req.get_response_api_sub(res_page['Items'], dic_element_name, dict_item_sub)
		print(result)
		#ページ毎のリクエスト結果取得
		# for res in res_page['Items']:
		# 	counter = counter + 1
		# 	# item = res['Item']
		# 	# name = item['itemName']
		# 	# price = item['itemPrice']
		# 	# print(f"NO. : {counter}　商品名: {name}　価格: {price}")
			
		# 	#商品をリスト化
		# 	item = [counter, name, price]
		# 	#商品リストに追加
		# 	itemList.append(item)
	#print(itemList)

	#最安値と最高値
	#print(list(map(lambda x:x[2],itemList)))
	min_price = min(list(map(lambda x:x[1],result)))
	max_price = max(list(map(lambda x:x[1],result)))
	print(f"最安値：{min_price}")
	print(f"最高値：{max_price}")

	#商品リストより最安値の商品と最高値の商品の取得
	min_price_item = []
	max_price_item = []
	for item_by_price in result:
		#print(item_by_price)
		#print(item_by_price[1])
		if min_price == item_by_price[1]:
			min_price_item.append(item_by_price)
		if max_price == item_by_price[1]:
			max_price_item.append(item_by_price)

	print(f"最安値の商品：{min_price_item}")
	print(f"最高値の商品：{max_price_item}")

	#戻り値 List（商品名、価格)
	return result

if __name__ == "__main__":
	keyword = "Pythonプログラミング入門"
	search_items(keyword)
