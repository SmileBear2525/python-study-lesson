import request as req

RAKUTEN_API_PRODUCT = "https://app.rakuten.co.jp/services/api/Product/Search/20170426"
APPLICATION_ID = "1017111620275786286"

def search_product(keyword: str):

	#課題３
	#リクエスト
	params = {
		"format": "jason",
		"applicationId": APPLICATION_ID,
		"keyword" : keyword	
	}

	#リクエスト実行
	response_product = req.get_api_param(RAKUTEN_API_PRODUCT, params)

	#レスポンス結果より取得する要素のセット
	dict_product = {'count':'検索結果数', 'page':'ページ', 'first':'ページ内商品始追番', 'last':'ページ内商品終追番', 'hits':'ヒット件数番','pageCount':'総ページ数'}

	#関数を使ってレスポンス情報取得
	req.get_response_api(response_product, dict_product)

	#リクエスト結果取得
	# print(f"検索数：{response_product['count']}")
	# print(f"ページ番号：{response_product['page']}")
	# print(f"ページ内商品始追番：{response_product['first']}")
	# print(f"ページ内商品終追番：{response_product['last']}")
	# print(f"ヒット件数番：{response_product['hits']}")
	# print(f"総ページ数：{response_product['pageCount']}")

	#リクエスト結果-製品取得
	#レスポンス結果より取得する要素のセット
	dic_element_name = 'Product'
	dict_product_sub = {'productName':'製品名', 'makerName':'メーカー名', 'maxPrice':'最高価格', 'minPrice':'最低価格'}

	#関数を使ってレスポンス情報のサブ階層取得
	result = req.get_response_api_sub(response_product['Products'], dic_element_name, dict_product_sub)
	# print(result)
	for rs in result:
		print(f"製品名：{rs[0]}")
		print(f"メーカー名：{rs[1]}")
		print(f"最高価格：{rs[2]}")
		print(f"最低価格：{rs[3]}")
		
	# for res_product in response_product['Products']:
	# 	product = res_product['Product']
	# 	print(f"製品名：{product['productName']}")
	# 	print(f"メーカー名：{product['makerName']}")
	# 	print(f"最高価格：{product['maxPrice']}")
	# 	print(f"最低価格：{product['minPrice']}")

	#戻り値 List（製品名、メーカー名, 最高価格, 最低価格)
	return result

if __name__ == "__main__":
	keyword = "Pythonプログラミング"
	search_product(keyword)

