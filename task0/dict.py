test_dict = {
	"名前": "りんご",
	"価格": 100,
	"個数": 3
}
print(test_dict["名前"])
print(test_dict["価格"])
print(test_dict["個数"])

item1 = {
	"名前": "りんご",
	"価格": 100,
	"個数": 3
}
item2 = {
	"名前": "ばなな",
	"価格": 200,
	"個数": 2
}
item3 = {
	"名前": "みかん",
	"価格": 150,
	"個数": 5
}
list_item = [item1, item2, item3]
print(list_item)

item_dict1 = {
	"商品名": "プレステ",
	"価格": 15000
}
item_dict2 = {
	"商品名": "ファミコン",
	"価格": 12000
}
item_dict3 = {
	"商品名": "スイッチ",
	"価格": 10000
}
item_list = [item_dict1, item_dict2, item_dict3]
def price_item(itemname):
	for item in item_list:
		if item["商品名"] == itemname:
			return item["価格"]
	return None

print(price_item("ファミコン"))
print(price_item("ゲームボーイ"))





