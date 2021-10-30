import time
from selenium import webdriver
import pandas
import datetime
from webdriver_manager.chrome import ChromeDriverManager
import threading

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

# スクライピング+CSV化関数（スレッド化）
def scraping_thread(driver, file_name):

	page_no = driver.find_element_by_class_name("pager__item--active").text
	log(f'{page_no} ページ目取得開始です')
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
	
	#次の画面へ遷移するURLの取得
	try:
		#下記はブラウザサイズによってはエラーになる
		#driver.find_element_by_class_name('iconFont--arrowLeft').click()
		link_next = driver.find_element_by_class_name('iconFont--arrowLeft').get_attribute("href")
		#画面遷移
		driver.get(link_next)
		print("画面遷移")
	except:
		log('最終ページのため、全取得完了')

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

	log(f'{driver.find_element_by_class_name("result__num").text} 件ヒット')

	# ヘッダのみ書き出し
	header_list = ["企業名","キャッチコピー","ステータス","仕事内容","対象となる方","勤務地","給与","情報更新日"]
	df = pandas.DataFrame(columns=header_list)
	df.to_csv(FLIE_NAME)

	thread_list = []
	elements = driver.find_elements_by_class_name("pager__item")
	for i in range((int(len(elements)/2)+1)):

		th = threading.Thread(target=scraping_thread, args=(driver, FLIE_NAME))
		th.start()
		time.sleep(10) #10秒待たないと遷移後のスクレイピングができない
		thread_list.append(th)

	# 全スレッドの終了を待ち受け
	for thread in thread_list:
	 		thread.join()

	driver.quit()

if __name__ == '__main__':
	scraping()
	