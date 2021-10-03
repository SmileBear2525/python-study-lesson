import random
import time
import eel

eel.init("web")
web_app_options = {"chromeFlags": ["--window-size=420,200"]}
#eel.start("main5.html", options=web_app_options, block=False)
eel.start("main5.html")

while True:
    eel.push_data([
        {"time": time.time() * 1000, "value": random.random()}, # JSのgetTime()と同じにするためミリ秒に直す
    ])
    eel.sleep(0.2)