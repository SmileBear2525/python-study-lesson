# 事前にgoogletransをインストールしておく
# 参考URL
# https://qiita.com/_yushuu/items/83c51e29771530646659
# https://sig9.hatenablog.com/entry/2021/08/26/000000
# pip install googletrans だとバージョンが古いため動かない
# pip uninstall googletrans アンインストール方法
# pip install googletrans=4.0.0-rc1 が最新バージョン

from googletrans import Translator
import eel

#課題１
def translate_input(word: str):
	translator = Translator()
	trans_word = translator.translate(text=word, src="en", dest="ja").text
	print(f"翻訳結果：{trans_word}")
	return trans_word

#Webアプリ用
def translate_input_lang(word: str, src_lang: str, dest_lang: str):
	translator = Translator()
	trans_word = translator.translate(text=word, src=src_lang, dest=dest_lang).text
	print(f"翻訳結果：{trans_word}")
	return trans_word

if __name__ == "__main__":
	en_words = input("英語を翻訳します。翻訳したい英語を入力してください：")
	translate_input(en_words)
	