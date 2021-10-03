
import os

#定数は大文字で定義
#csvファイルのパス
SOURCE_CSV_PATH = "source2.csv"
#csvが存在しない場合の初期データ
DEFAULT_CARACTORS = ["ぜんいつ","たんじろう","ねずこ","いのすけ"]

def write_source(csv_path:str, source:list):
	'''
	sourceをcsvに書き込む
	'''
	with open(csv_path, mode='w', encoding='utf-8') as f:
		f.write("\n".join(source)) #listを改行で連結してファイルに書き込む


def read_source(csv_path:str):
	'''
	sourceをCSVから読み込む
	'''
	if not os.path.exists(csv_path):
		print(f'パス：{csv_path}が存在しません。新規作成します')
		write_source(csv_path, DEFAULT_CARACTORS)
	#ファイル読み込み
	with open(csv_path, mode='r', encoding='utf-8') as f:
		return f.read().splitlines() #readでファイルを読み込み、splitlinesで１行づつに分解してlistとして返す

def search():
	'''
	検索処理
	'''
	# sourceをCSVから読み込む
	source = read_source(SOURCE_CSV_PATH)

	# White Trueにすると無限に繰り返す
	#while True:
	word = input('鬼滅の登場人物を入力＞＞')
	#search
	if word in source:
		print(f'{word}は登録されています')
	else:
		print(f'{word}は未登録です')
		#add
		is_add = input('追加しますか？(n:いいえ,y:はい＞＞')
		if is_add  == 'y':
			source.append(word)
	
		#sourcをcsvに書き込む
		write_source(SOURCE_CSV_PATH, source)

if __name__ == '__main__':
	search()