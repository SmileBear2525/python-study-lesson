from os import system
import eel
import desktop
import pos

app_name="web"
html_name="cashregister.html"
screen_size=(700,600)

ITEM_MASTER_LIST_PATH = './itemlist.csv'

@eel.expose
def input_csv():
	print("ここから")

	# グローバル変数の使用宣言
	global system_order
	item_master_list = pos.input_csv(ITEM_MASTER_LIST_PATH)
	system_order = pos.Order(item_master_list)
	input_status = True
	eel.msg_input_master_item(input_status)

@eel.expose
def display_item(no_code):
	print("商品表示")
	print(no_code)

	add_item = system_order.get_item(no_code)
	if add_item == None:
		message_order = "商品コードが存在しません、入力し直してください"
		result_order = False
	else:
		message_order = "商品番号：{}　商品名：{}　値段：{}".format(add_item.no, add_item.name, add_item.price)
		result_order = True
	eel.msg_result_order_items(result_order, message_order)

@eel.expose
def add_order_list(no_code,count):
	print("python add_order_listにきたよ")
	add_item = system_order.add_order_count(no_code, count)
	message_add_order = "商品番号：{}　商品名：{}　値段：{}　購入数：{}\n".format(add_item[0].no, add_item[0].name, add_item[0].price, add_item[1])
	eel.msg_add_order_items(message_add_order)

# オーダのクリア
@eel.expose
def clear_order_list():
	system_order.clear_order_count()

# 購入値段の出力
@eel.expose
def calc_order_list():
	price_total = system_order.calc_order_list()
	eel.msg_total_price(price_total)

# 精算
@eel.expose
def pay_price(pay_price):
	change_price = system_order.calc_change_money(pay_price)
	eel.msg_change_price(change_price)

@eel.expose
def output_receipt(total_price, deposit_price):
	print("レシート出力します")
	receipt_file_name = system_order.output_receipt_sheet(total_price, deposit_price)
	eel.msg_receipt_file(receipt_file_name[0], receipt_file_name[1])

desktop.start(app_name, html_name, screen_size)

#if __name__ == "__main__":
# pos.init_possystem()