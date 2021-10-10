import eel
import socket
import sys

# eel起動時のオプションについて参考資料
# https://qiita.com/hakki600/items/38e3b870f15677b3a6e0

ALLOW_EXTENSIONS = ['.html', '.css', '.js', '.ico'] #拡大を許可？
CHROME_ARGS = [
    '--incognit',  # シークレットモード
    '--disable-http-cache',  # キャッシュ無効
    '--disable-plugins',  # プラグイン無効
    '--disable-extensions',  # 拡張機能無効
    '--disable-dev-tools',  # デベロッパーツールを無効にする
]

def start(appName, htmlName, size): #画面生成
	#eel.init(appName)
	#eel.start(htmlName)

	eel.init(appName, allowed_extensions=ALLOW_EXTENSIONS)

	#未使用ポート取得
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('',0))
	port = s.getsockname()[1]
	s.close()
	options = {
		'mode': "chrome",
		'close_callback': exit,
		'port':port,
		'cmdline_args':CHROME_ARGS		
	}
	
	eel.start(htmlName, options=options, size=size, suppress_error=True)

def exit(arg1, arg2):
	sys.exit(0)
