import requests

#リクエスト関数
def get_api(url):
	result = requests.get(url)
	return result.json()

#レスポンス結果より上位階層の情報をリスト化
def get_response_api(response, dictionay):
	#response_list = []
	dic_list = []
	try:
		for key,value in dictionay.items():
			# print(value)
			# print(response[key])
			# print(f"{value}：{response[key]}")
			#リスト化
			value_list = [value, response[key]]
			dic_list.append(value_list)
		return dic_list
	except Exception as e:
		return []

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