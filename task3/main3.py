import eel
import numpy as np

# フォルダ構成で作ったWebファイルを読み込む
eel.init("web")

list = np.random.rand(8).tolist()
print(list)
eel.js_function(list)

eel.js_function_return()(lambda val: print(val + " from Javascript"))

# main.htmlを読み込んでellをスタート
eel.start("main3.html")