#javascriptからPython関数を呼び出す

import eel

@eel.expose
def python_function(val):
	print(val + " from Javascript")
def python_function2():
	return "Hello"

eel.init("web")
eel.start("main4.html")