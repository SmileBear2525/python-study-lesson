# Pythonからjavascriptの関数を呼び出す

import eel
import numpy as np

def main():
	eel.init("web")
	eel.start("main2.html")

@eel.expose
def open_window():
	eel.start("main2.html")

if __name__ == '__main__':
	main()

