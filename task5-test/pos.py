#レジシステム構築
#オーダーをクラス化する
import pandas as pd
import sys
import datetime
import os

#商品情報クラス
class Item:
	#コンストラクタ
	def __init__(self, no, name, price):
		self.no = no
		self.name = name
		self.price = price

#オーダークラス
class Order:
	def __init__(self, item_master_list):
		self.item_master_list = item_master_list
		self.item_order_list = [] #オーダー商品リスト（[オーダーItem,購入数]のリスト）

	#オーダー登録した商品を表示する（課題１）
	def get_item(self, no_order):
		print("pos.get_itemにきました")
		for item in self.item_master_list:
			if str(item.no) == no_order:
				print(item.no)
				print(no_order)
				print("商品番号が一致しました")
				print("商品番号:{}　商品名{}　値段{}".format(item.no, item.name, item.price))
				return item
		#商品が一致しない
		print("商品番号が一致しませんでした")
		return None
	
	# 商品コード、購入数の購入リストへ追加
	def add_order_count(self, no_order, item_count):
		add_item = self.get_item(no_order)
		if add_item != None:
			add_item = [add_item, item_count]
			self.item_order_list.append(add_item) #個数も入力
		return add_item

	# 商品コード、購入数の購入リストへ追加
	def clear_order_count(self):
		self.item_order_list.clear() #オーダーリストのクリア
	

	#購入したものの合計金額を出す
	def calc_order_list(self):
		print("トータル金額を表示します")
		price_total = 0
		for order in self.item_order_list:
			price_total += int(order[0].price) * int(order[1])
		receipt_data_totalprice = "合計金額：{}".format(price_total)
		print(receipt_data_totalprice)
		return price_total

	def output_receipt_sheet(self, order_total_price, deposit_price):
		print("出力開始")
		write_receipt("購入商品一覧\n")
		write_receipt("--------------------\n")
		for order in self.item_order_list:
			receipt_data_order_list = "商品番号:{}　商品名：{}　値段：{}----購入数{}".format(order[0].no, order[0].name, order[0].price, order[1])
			write_receipt(receipt_data_order_list + "\n")
		write_receipt("--------------------\n")
		receipt_data_totalprice = "合計金額：{}".format(order_total_price)
		write_receipt(receipt_data_totalprice + "\n")
		write_receipt("お預かり金額：{}\n".format(deposit_price))
		write_receipt("おつり：{}\n".format(int(deposit_price)-int(order_total_price)))
		write_receipt("--------------------\n")
		write_receipt("ありがとうございました\n")
		file_list = [RECEIPT_FOLDER_SUBPATH, DATETIME_FULE_NAME]
		return file_list

# -----
# 商品マスタをCSVから登録
def input_csv(path):
	print("商品マスタCSVの登録")
	#●ディクショナリーを使ったやり方
	#●item_master_list = dict()
	#商品情報にクラスを使う
	item_master_list = []
	try:
		item_master_list_csv =  pd.read_csv(path, dtype={"no":object})
		print(item_master_list_csv)

		for item_no_csv,item_name_csv,item_price_csv in zip(list(item_master_list_csv["no"]), list(item_master_list_csv["name"]), list(item_master_list_csv["price"])):
			#●item_master_list[item_no] = [item_name, item_price]
			item_master_list.append(Item(item_no_csv, item_name_csv, item_price_csv))
		print("商品マスタの登録完了")
		return item_master_list
	except:
		print("商品マスタの登録に失敗しました")
		sys.exit()

#レシートに書き出し
#RECEIPT_FOLDER_PATH = './receipt'
RECEIPT_FOLDER_PATH = './web'
RECEIPT_FOLDER_SUBPATH = '/receipt'
DATETIME_FULE_NAME = "receipt_" + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + ".txt"
def write_receipt(text):
	#ディレクトリ存在チェック
	if not os.path.exists(RECEIPT_FOLDER_PATH + RECEIPT_FOLDER_SUBPATH):
		print("{}ディレクトリを作成します".format(RECEIPT_FOLDER_PATH + RECEIPT_FOLDER_SUBPATH))
		os.makedirs(RECEIPT_FOLDER_PATH + RECEIPT_FOLDER_SUBPATH)
	write_receipt_path = RECEIPT_FOLDER_PATH + RECEIPT_FOLDER_SUBPATH + "/" + DATETIME_FULE_NAME
	#print("出力ファイル名：{}".format(write_receipt_path))
	with open(write_receipt_path, "a") as f:
		f.write(text)