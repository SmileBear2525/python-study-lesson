# ファイルopen
import pathlib

p_new = pathlib.Path('temp/new_file.txt')
print(p_new.exists())
with p_new.open(mode='w') as f:
	f.write('line 1\nline 2\nline 3\n')

with p_new.open() as f:
	print(f.read())

# テキストファイルの読み込み、書き込み
s = p_new.read_text()

print(s)
print(type(s))

i = p_new.write_text('new text') #追加ではなく上書き
print(i) # 書き込んだ文字列が返される
print(type(i))
print(p_new.read_text())

p_new2 = pathlib.Path('temp/new_file2.txt')
print(p_new2.exists())
#print(p_new2.read_text())

# 一行ずつ読み込んだり、追記する必要がなければ、open()よりもread_text()、write_text()の方が遥かに楽

# ファイルを削除
##p_empty = pathlib.Path('temp/empty_file.txt')
##print(p_empty.exists())
##p_empty.unlink() #存在しないファイルに対してはエラー、またpathも削除しようとするとエラー
##print(p_empty.exists())

# ディレクトリ内のファイルを一括削除
##p_dir = pathlib.Path('temp/')
##for p in p_dir.iterdir():
##	print(p)
##	if(p.is_file()):
##		p.unlink()

#open() withによるファイル読み書き
textpath = 'temp/new_dir/empty_file.txt'
f = open(textpath)
print(type(f))
f.close()

#↓↓↓同じ↓↓↓
# こちらはclose()は必要ない、withブロックが終了すると終了時に自動的にクローズされる
with open(textpath) as f: 
	print(type(f))

#encording エンコーディング
import locale
print(locale.getpreferredencoding())



