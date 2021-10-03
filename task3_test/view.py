import eel
import search
import desktop

app_name="web"
html_name="search.html"
size=(700,600)

@eel.expose
def python_search(keyword, file):
	print("ここから")
	return search.python_search(keyword, file)

desktop.start(app_name, html_name, size)