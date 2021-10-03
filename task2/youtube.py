#youtubeによる講座
#https://www.youtube.com/watch?v=J-wYKEUB-w8

from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import pandas
from webdriver_manager.driver import ChromeDriver, Driver

def scraping():
	#Chromeドライバーのインストール
	deriver_path = ChromeDriverManager().install()
	options = ChromeOptions()
	options.add_argument("--headless")
	options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36")
	driver = Chrome(deriver_path,options=options)
	driver.get('https://gyoumu-kouritsuka-pro.site/')
	
	df = pandas.DataFrame()
	while True:
		article_elems = driver.find_elements_by_css_selector('.entry-card-wrap.a-wrap.border-element.cf')
		for article in article_elems:
			#print(article.text)
			title = article.find_element_by_tag_name('h2').text
			data = article.find_element_by_class_name('post-date').text
			#こっちでもよい
			# data = article.find_element_by_css_selector('.post-date').text
			link = article.get_attribute('href')
			print(title, data, link)

			df = df.append({
				"タイトル" : title,
				"日時" : data,
				"リンク" : link
			}, ignore_index=True)

		try:
			driver.find_element_by_css_selector('.pagination-next-link.key-btn').click()
		except:
			print('最終ページ')
			break

	df.to_csv("記事一覧.csv", encoding="utf-8_sig")


scraping()