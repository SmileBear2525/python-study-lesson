#レジシステム構築
#オーダーをクラス化しないやり方
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

item_master_list = []

# 商品マスタをCSVから登録
def input_csv(path):
	print("商品マスタCSVの登録")
	#●ディクショナリーを使ったやり方
	#●item_master_list = dict()
	#商品情報にクラスを使う
	#item_master_list = []
	try:
		item_master_list_csv =  pd.read_csv(path, dtype={"no":object})
		print(item_master_list_csv)

		for item_no_csv,item_name_csv,item_price_csv in zip(list(item_master_list_csv["no"]), list(item_master_list_csv["name"]), list(item_master_list_csv["price"])):
			#●item_master_list[item_no] = [item_name, item_price]
			item_master_list.append(Item(item_no_csv, item_name_csv, item_price_csv))
		print("商品マスタの登録完了")
	except:
		print("商品マスタの登録に失敗しました")
		sys.exit()

#オーダー登録した商品を表示する（課題１）
def get_item(no_order):
	for item in item_master_list:
		if str(item.no) == no_order:
			print(item.no)
			print(no_order)
			print("商品番号が一致しました")
			print("商品番号:{}　商品名{}　値段{}".format(item.no, item.name, item.price))
			return item
	#商品が一致しない
	print("商品番号が一致しませんでした")
	return None

#オーダーをコンソールから入力（課題２）
order_list = [] #[Item,個数]の二次元配列
def console_input():
	dic={'y':True,'yes':True,'n':False,'no':False}
	print("商品一覧はこちらです")
	for item in item_master_list:
		print("商品番号:{}　商品名{}　値段{}".format(item.no, item.name, item.price))
	
	while True:
		try:
			check = input('商品を購入しますか？[Y]es/[N]：').lower()
			if dic[check] == True:
				input_no_order= input('商品番号を入力してください：')
				item_check = get_item(input_no_order)
				if item_check != None:
					
					while True:
						count_order = input("購入数を入力してください：")
						try:
							if count_order.isdigit(): #数字だったら
								add_item = [item_check,count_order]
								order_list.append(add_item) #個数も入力
								print("購入リスト：{},{}".format(item_check.no, count_order))
								break
							else:
								print("数字が入力されていません")
								break
						except:
							pass
							break

			elif dic[check] == False:
				print("商品購入を終了します。ありがとうございました")
				break
		except:
			print("正しない文字が入力されたため終了します")
			break

#オーダーリストの表示
def view_order_list():
	print("オーダーした商品および個数を表示します")
	if order_list == False:
		print("購入オーダーはありません")
	else:
		write_receipt("購入商品一覧\n")
		write_receipt("--------------------\n")
		for order in order_list:
			receipt_data_order_list = "商品番号:{}　商品名：{}　値段：{}----購入数{}".format(order[0].no, order[0].name, order[0].price, order[1])
			print(receipt_data_order_list)
			write_receipt(receipt_data_order_list + "\n")
		write_receipt("--------------------\n")
		#calc_order_list()

#購入したものの合計金額を出す
def calc_order_list():
	print("トータル金額を表示します")
	price_total = 0
	for order in order_list:
		price_total += int(order[0].price) * int(order[1])
	receipt_data_totalprice = "合計金額：{}".format(price_total)
	print(receipt_data_totalprice)
	write_receipt(receipt_data_totalprice + "\n")
	return price_total

#お客さんよりお預かりした金額を入力
def input_pay_money():
	while True:
		pay_money = input("お客さんが支払った金額を入力してください：")
		if pay_money.isdigit():
			print("{}円　お預かりしました".format(pay_money))
			break
		else:
			print("金額が入力されていません、入力し直してください")
	return pay_money

#おつりの計算
def calc_change_money():
	price_total = calc_order_list()
	while True:
		if int(price_total) == 0:
			print("商品の購入はありませんでした")
			break
		pay_money = input_pay_money()
		change_money = int(pay_money) - int(price_total)
		if int(change_money) == 0:
			print("購入頂き、ありがとうございました。")
			write_receipt("支払い金額：{}\n".format(pay_money))
			write_receipt("おつり：{}\n".format(change_money))
			break
		elif int(change_money) > 0:
			print("{}円のお釣りです。ありがとうございました。".format(change_money))
			write_receipt("支払い金額：{}\n".format(pay_money))
			write_receipt("おつり：{}\n".format(change_money))
			break
		else:
			print("{}円の不足しています。再度、入力してください".format(change_money))

#レシートに書き出し
RECEIPT_FOLDER_PATH = './receipt'
DATETIME_FULE_NAME = "receipt_" + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + ".txt"
def write_receipt(text):
	#ディレクトリ存在チェック
	if not os.path.exists(RECEIPT_FOLDER_PATH):
		print("{}ディレクトリを作成します".format(RECEIPT_FOLDER_PATH))
		os.makedirs(RECEIPT_FOLDER_PATH)
	write_receipt_path = RECEIPT_FOLDER_PATH + "/" + DATETIME_FULE_NAME
	#print("出力ファイル名：{}".format(write_receipt_path))
	with open(write_receipt_path, "a") as f:
		f.write(text)


def main():
		#商品マスタをCSVから登録（課題３）
	input_csv(ITEM_MASTER_LIST_PATH)
	#オーダー取得
	#get_item("001")
	#コンソールよりオーダー登録
	console_input()
	#オーダー一覧表示
	view_order_list()
	#オーダー計算
	#calc_order_list()
	#支払い金額の入力
	#input_pay_money()
	#おつり計算
	calc_change_money()



ITEM_MASTER_LIST_PATH = './itemlist.csv'
if __name__ == "__main__":
	main()
	#write_receipt("あああ")