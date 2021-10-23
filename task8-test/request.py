import requests

#リクエスト関数(パラメータ使用)
def get_api_param(url, params: dict):
	# APIを実行
	result = requests.get(url, params=params)
	# 結果のjsonをdict化
	return result.json()

#レスポンス結果よりサブ階層の情報取得をリスト化
def get_response_api_sub(response, element_name, dictionay):
	result_list = []
	try:
		for res in response:
			r = res[element_name]
			value_list = []
			for key,value in dictionay.items():
				# print(key)
				# print(r[key])
				# print(f"{value}：{r[key]}")
				value_list.append(r[key])
			result_list.append(value_list)
		return result_list
	except Exception as e:
		return []