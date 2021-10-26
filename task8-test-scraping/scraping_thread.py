import time
from selenium import webdriver
import pandas
import datetime
from webdriver_manager.chrome import ChromeDriverManager
import threading
import queue

FILENAME_DATETIME = datatime=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
LOG_FILE_PATH = f'./log/log_{FILENAME_DATETIME}.log'

###ログ出力用関数
def log(txt):
	dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	with open(LOG_FILE_PATH, mode='a', encoding="UTF-8") as f:
		logStr = "[%s:%s] %s" % ('log', dt, txt)
		print(txt)
		f.write(logStr + "\n")

def get_element(driver, element_company_list, q):
	page_no = driver.find_element_by_class_name("pager__item--active").text
	log(f'{page_no} ページ目取得開始です')

	company_list = driver.find_elements_by_class_name('cassetteRecruit__name')
	title_list = driver.find_elements_by_class_name('cassetteRecruit__copy')
	employment_list = driver.find_elements_by_class_name('labelEmploymentStatus')
	jobtable_list = driver.find_elements_by_css_selector('table.tableCondition')
	updata_list = driver.find_elements_by_class_name('cassetteRecruit__endDate')
	
	for company,title,employment,jobtable,updata in zip(company_list,title_list,employment_list,jobtable_list,updata_list):
		element_company_list.append(company.text)
		#element_tilte_list.append(title.find_element_by_tag_name('a').text)
		#element_employment_list.append(employment.text)
		#bodys = jobtable.find_elements_by_css_selector('td.tableCondition__body')
		#element_job_list.append(bodys[1].text)
		#element_user_list.append(bodys[2].text)
		#element_place_list.append(bodys[3].text)
		#element_cost_lsit.append(updata.find_element_by_tag_name('span').text)
	log(f'{page_no} ページ目取得終了です')

	q.put(element_company_list)
	#return element_company_list, element_tilte_list, element_employment_list, element_job_list, element_user_list, element_place_list, element_cost_lsit


def scraping():
	options = webdriver.ChromeOptions()
	options.add_argument('--headless')

	#driver = webdriver.Chrome(options=options)
	driver = webdriver.Chrome(ChromeDriverManager().install())

	driver.get('https://tenshoku.mynavi.jp/')
	log(f'サイト名:{driver.title}')

	search_keyword = input_key()

	log(f'検索キーワード：{search_keyword}')
	search = driver.find_element_by_class_name('topSearch__text')
	search.send_keys(search_keyword)
	search.submit()
	time.sleep(3)
	
	log(f'{driver.find_element_by_class_name("result__num").text} 件ヒット')

	element_company_list = []
	element_tilte_list = []
	element_employment_list = []
	element_job_list = []
	element_user_list = []
	element_place_list = []
	element_cost_lsit = []

	

	while True:

		#element_company_list, element_tilte_list, element_employment_list, element_job_list, element_user_list, element_place_list, element_cost_lsit = get_element(driver, element_company_list, element_tilte_list, element_employment_list, element_job_list, element_user_list, element_place_list, element_cost_lsit)
		
		q = queue.Queue()
		th = threading.Thread(target=get_element, args=(driver, element_company_list, q))
		th.start()
		try:
			driver.find_element_by_class_name('iconFont--arrowLeft').click()
		except:
			log('最終ページのため、全取得完了')
			break

	thread_list = threading.enumerate()
	thread_list.remove(threading.main_thread())
	print(thread_list)
	for thread in thread_list:
		thread.join()
		print(q.get())
	
	#output_company_list = []
	#[r[0] for r in output_list]
	#print(element_company_list)

	# df = pandas.DataFrame({
	# 	"企業名":output_list[0],
	# 	"キャッチコピー":output_list[1],
	# 	"ステータス":output_list[2],
	# 	"仕事内容":output_list[3],
	# 	"対象となる方":output_list[4],
	# 	"勤務地":output_list[5],
	# 	"給与":output_list[6],
	# 	"情報更新日":output_list[7]
	# })

	# print(df)

	#df.to_csv(f'求人一覧_{search_keyword}_{FILENAME_DATETIME}.csv')
	#driver.quit()

def input_key():
	key_word = input('検索するキーワードを入力してください：')
	return key_word

if __name__ == '__main__':
	scraping()
	