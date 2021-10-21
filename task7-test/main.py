from googletrans import Translator
from os import system
import eel
import desktop
import translate

app_name="web"
html_name="translate.html"
screen_size=(600,500)

@eel.expose
def translete_inputtext(word, before_lang, afer_lang):
	translate_word = translate.translate_input_lang(word, before_lang, afer_lang)
	eel.txt_result_word(translate_word)


desktop.start(app_name, html_name, screen_size)