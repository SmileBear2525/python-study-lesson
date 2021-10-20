from api2 import search_items
from api3 import search_product
from api4 import rankingList_to_csv

#テスト実行
#python -m pytest ファイル名::テストしたい関数 -s

def test_search_items():
	keyword = "Pythonプログラミング入門"

	#戻り値 List（商品名、価格)
	res = search_items(keyword)

	assert len(res)
	assert len(res[0][0]) > 0 #商品名
	assert res[0][1] >0 #価格

def test_search_product():
	keyword = "Pythonプログラミング入門"

	#戻り値 List（製品名、メーカー名, 最高価格, 最低価格)
	res = search_product(keyword)

	assert len(res)
	assert res[0][2] > res[0][3] #最高価格 > 最低価格

def test_rankingList_to_csv():
	genre_id = "551167"

	#戻り値 List（ランク、商品名、価格、キャッチコピー、商品URL、ショップ名)
	res = rankingList_to_csv(genre_id)
	print(res)

	assert len(res)
	assert res[0][0] == 1 #ランク
	assert res[1][0] == 2 #ランク
	assert int(res[0][2]) >0 #価格
	assert res[0][4].startswith("http") #URL部分検索

