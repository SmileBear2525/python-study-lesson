# 課題１：簡単な検索ツールの作成

import pathlib
import csv

# キャラクターリスト
source = ['ロナウド', 'メッシ', 'ルーニー', 'ガスコイン', 'クライフ', 'ジーコ']

# 検索関数
def input_source():
	return input('好きなサッカー選手を入力してください：')

def search_soruce(player):
	#検索
	if player in source:
		print(f'{player}は存在しています')
	else:
		print(f'{player}は存在していないので、追加します')
		source.append(player) 
	display_source()

# キャラクター一覧表示
def display_source():
	print(source)

# キャラクターファイル読み込み
def readfile_source():
	path_r = pathlib.Path('temp/memberlist.csv')
	with open(path_r) as f:
		memberlist = csv.reader(f)
		for member_row in memberlist:
			for member in member_row:
				print(member)
				search_soruce(member)


# キャラクターファイル書き込み
def writefile_source():
	path_w = pathlib.Path('temp/write_memberlist.csv')
	with open(path_w, mode='w') as f:
		f.write("".join(source))
	display_source()

if __name__ == '__main__':
	input = input_source()
	search_soruce(input)
	#readfile_source()
	#writefile_source()
