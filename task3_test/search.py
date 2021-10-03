import eel
import pandas

def python_search(keyword, file):
	print("ここにきたよ")
	#CSVファイルから検索対象を取得
	read_file = pandas.read_csv(file)
	name_list = list(read_file["name"])

	#検索
	if keyword in name_list:
		str_found = "「{}」はあります".format(keyword)
		print(str_found)
		return str_found
		
	else:
		str_notfound = "「{}」はありません".format(keyword)
		name_list.append(keyword)
		str_notfound += "\n「{}」を追加します".format(keyword)
		print(str_notfound)

		#CSV書き込み
		df=pandas.DataFrame(name_list, columns=["name"])
		df.to_csv(file, encoding='utf-8')
		print(name_list)
		return str_notfound
		
#eel.init("web")
#eel.start("search.html")