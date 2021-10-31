import time
from selenium import webdriver
import pandas
import datetime
from webdriver_manager.chrome import ChromeDriverManager
import threading
from concurrent.futures import ThreadPoolExecutor

FILENAME_DATETIME = datatime=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
LOG_FILE_PATH = f'./log/log_{FILENAME_DATETIME}.log'

###ログ出力用関数
def log(txt):
	dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	with open(LOG_FILE_PATH, mode='a', encoding="UTF-8") as f:
		logStr = "[%s:%s] %s" % ('log', dt, txt)
		print(txt)
		f.write(logStr + "\n")

# 検索キーワード入力関数
def input_key():
	key_word = input('検索するキーワードを入力してください：')
	return key_word

# 検索キーワード入力関数
def input_max_workers():
	max_workers = input('スレッドの最大数を指定してください：')
	return max_workers


# スクライピング+CSV化関数
def scraping_thread(url, file_name):
	print('scrapint_thread')
	print(url)
	options = webdriver.ChromeOptions()
	options.add_argument('--headless')
	driver = webdriver.Chrome(ChromeDriverManager().install())

	#画面遷移
	driver.get(url)
	print("画面遷移")

	page_no = driver.find_element_by_class_name("pager__item--active").text
	log(f'{page_no} ページ目取得開始です')

	#スクレイピング
	output_company_list = []
	output_title_list = []
	output_employment_list = []
	output_jobtable_job_list = []
	output_jobtable_user_list = []
	output_jobtable_place_list = []
	output_jobtable_cost_list = []
	output_updata_list = []

	company_list = driver.find_elements_by_class_name('cassetteRecruit__name')
	title_list = driver.find_elements_by_class_name('cassetteRecruit__copy')
	employment_list = driver.find_elements_by_class_name('labelEmploymentStatus')
	jobtable_list = driver.find_elements_by_css_selector('table.tableCondition')
	updata_list = driver.find_elements_by_class_name('cassetteRecruit__endDate')

	for company,title,employment,jobtable,updata in zip(company_list,title_list,employment_list,jobtable_list,updata_list):
		output_company_list.append(company.text)
		output_title_list.append(title.find_element_by_tag_name('a').text)
		output_employment_list.append(employment.text)
		bodys = jobtable.find_elements_by_css_selector('td.tableCondition__body')
		output_jobtable_job_list.append(bodys[0].text)
		output_jobtable_user_list.append(bodys[1].text)
		output_jobtable_place_list.append(bodys[2].text)
		output_jobtable_cost_list.append(bodys[3].text)
		output_updata_list.append(updata.find_element_by_tag_name('span').text)

	log(f'{page_no} ページ目取得終了です')

	#CSV書き込み
	df = pandas.DataFrame({
		"企業名":output_company_list,
		"キャッチコピー":output_title_list,
		"ステータス":output_employment_list,
		"仕事内容":output_jobtable_job_list,
		"対象となる方":output_jobtable_user_list,
		"勤務地":output_jobtable_place_list,
		"給与":output_jobtable_cost_list,
		"情報更新日":output_updata_list
	})
	df.to_csv(file_name, mode='a', header=False)

	#driverクローズ
	driver.close()
	
def scraping():
	options = webdriver.ChromeOptions()
	options.add_argument('--headless')

	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.get('https://tenshoku.mynavi.jp/')
	log(f'サイト名:{driver.title}')

	search_keyword = input_key()
	log(f'検索キーワード：{search_keyword}')
	search = driver.find_element_by_class_name('topSearch__text')
	search.send_keys(search_keyword)
	search.submit()
	time.sleep(3)
	FLIE_NAME = f'求人一覧_{search_keyword}_{FILENAME_DATETIME}.csv'

	log(f'{driver.find_element_by_class_name("result__num").text} ヒット')

	# ヘッダのみ書き出し
	header_list = ["企業名","キャッチコピー","ステータス","仕事内容","対象となる方","勤務地","給与","情報更新日"]
	df = pandas.DataFrame(columns=header_list)
	df.to_csv(FLIE_NAME)

	#スレッド数最大指定
	max_thread = input_max_workers()
	tpe = ThreadPoolExecutor(max_workers=int(max_thread))
	
	thread_list = []
	elements = driver.find_elements_by_class_name("pager__item")
	for i in range((int(len(elements)/2)+1)):
		if i == 0:
			#検索結果最初の画面をスクレイピングのため、現在ページのURLを取得
			url = driver.current_url
		else:
			#画面遷移後のスクレイピングを行うため、次ページのURL取得
			#time.sleep(5)
			url = elements[i-1].find_element_by_tag_name('a').get_attribute("href")
		
		# 処理前の時刻
		t1 = time.time()

		#スクレイピング+CSV化関数呼び出し
		#scraping_thread(url, FLIE_NAME)
		tpe.submit(scraping_thread, url, FLIE_NAME)
		#th = threading.Thread(target=scraping_thread, args=(url, FLIE_NAME))
		#th.start()
		#thread_list.append(th)

		# 処理後の時刻
		t2 = time.time()
		elapsed_time =t2 - t1
		print(f"計測時間：{elapsed_time}")

	# 全スレッドの終了を待ち受け
	#for thread in thread_list:
	# 		thread.join()

	driver.quit()
	log("完了")

if __name__ == '__main__':
	scraping()