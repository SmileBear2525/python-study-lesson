# https://gammasoft.jp/support/css-selector-for-python-web-scraping/

from bs4 import BeautifulSoup

html = """
<h3 class="ramen title" summary="メニュー">ラーメンメニュー</h3>
<ul>
  <li id="syouyu" class="ramen item">醤油ラーメン</li>
  <li id="miso" class="ramen item">味噌ラーメン</li>
</ul>
"""

soup = BeautifulSoup(html, "html.parser")
#タイプセレクタ
print(soup.select("h3"))
print(soup.select("li"))
#idセレクタ
print(soup.select("#syouyu"))
#classセレクタ
print(soup.select(".ramen"))
#属性セレクタ
print(soup.select("[class='ramen title']"))
print(soup.select("[class='ramen item']"))
print(soup.select("[id='miso']"))
print(soup.select("[class='ramen2']"))
print(soup.select("[class*='ramen']")) #ramenを含む全ての要素
print(soup.select("[summary='メニュー']"))

#属性による修飾
print(soup.select("li.ramen.item"))
print(soup.select("li#miso"))
print(soup.select("h3[summary='メニュー']"))

#子孫•子セレクタ
print(soup.select("ul li"))

#グループ化
print(soup.select("h3, ul"))
print(soup.select("#syouyu, #miso"))



