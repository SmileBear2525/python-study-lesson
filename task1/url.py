# Web上のファイルをダウンロード
import os
import pprint
import time
# ssl認証に関するエラーの対処法
# https://qiita.com/DisneyAladdin/items/9733a7e640a175c23f39
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.error
import urllib.request

# URLと保存先パスを指定してファイルをダウンロード、ダウンロードたファイルをローカルに保存
def download_file(url, dst_path):
	try:
		with urllib.request.urlopen(url) as web_file:
			data = web_file.read()
			with open(dst_path, mode='wb') as local_file: #wb:バイナリの書き込み
				local_file.write(data)
	except (urllib.error.URLError, IsADirectoryError) as e:
		print(e)


url = 'https://www.python.org/static/img/python-logo.png'
dst_path = 'temp/py-logo.png'
download_file(url, dst_path)

# 保存先のディレクトリを指定してURLのファイル名で保存
def download_file_to_dir(url, dst_dir):
	print(os.path.join(dst_dir, os.path.basename(url)))
	download_file(url, os.path.join(dst_dir, os.path.basename(url)))

dst_dir = 'temp'
download_file_to_dir(url,dst_dir) 

#URLが存在しない場合の例外エラー
url_error = 'https://www.python.org/static/img/python-logo_xxx.png'
download_file_to_dir(url_error, dst_dir)

# ディレクトリが存在しない場合の例外エラー
url = 'https://www.python.org/static/img/python-logo.png'
dst_path2 = 'temp/'
download_file(url,dst_path2) 

# format書式変換
# https://note.nkmk.me/python-format-zero-hex/
num_list = ['{:03}.jpg'.format(i) for i in range(5)]
print(num_list)

