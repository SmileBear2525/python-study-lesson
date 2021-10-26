import time
from selenium import webdriver
import pandas
import datetime
from webdriver_manager.chrome import ChromeDriverManager

FILENAME_DATETIME = datatime=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
LOG_FILE_PATH = f'./log/log_{FILENAME_DATETIME}.log'

###ログ出力用関数
def log(txt):
	dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	with open(LOG_FILE_PATH, mode='a', encoding="UTF-8") as f:
		logStr = "[%s:%s] %s" % ('log', dt, txt)
		print(txt)
		f.write(logStr + "\n")


def scraping():
	options = webdriver.ChromeOptions()
	options.add_argument('--headless')

	#driver = webdriver.Chrome(options=options)
	driver = webdriver.Chrome(ChromeDriverManager().install())

	driver.get('https://tenshoku.mynavi.jp/')
	log(f'サイト名:{driver.title}')

	search_keyword = input_key()
	#search_keyword = 'アメリカン　エキスプレス'
	log(f'検索キーワード：{search_keyword}')
	search = driver.find_element_by_class_name('topSearch__text')
	search.send_keys(search_keyword)
	search.submit()
	time.sleep(3)
	
	log(f'{driver.find_element_by_class_name("result__num").text} 件ヒット')

	output_company_list = []
	output_title_list = []
	output_employment_list = []
	output_jobtable_job_list = []
	output_jobtable_user_list = []
	output_jobtable_place_list = []
	output_jobtable_cost_list = []
	output_jobtable_firstcost_list = []
	output_updata_list = []

	while True:

		page_no = driver.find_element_by_class_name("pager__item--active").text
		log(f'{page_no} ページ目取得開始です')

		company_list = driver.find_elements_by_class_name('cassetteRecruit__name')
		title_list = driver.find_elements_by_class_name('cassetteRecruit__copy')
		employment_list = driver.find_elements_by_class_name('labelEmploymentStatus')
		jobtable_list = driver.find_elements_by_css_selector('table.tableCondition')
		updata_list = driver.find_elements_by_class_name('cassetteRecruit__endDate')
		
		for company,title,employment,jobtable,updata in zip(company_list,title_list,employment_list,jobtable_list,updata_list):
			#print(company.text)
			output_company_list.append(company.text)
			#print(title.find_element_by_tag_name('a').text)
			output_title_list.append(title.find_element_by_tag_name('a').text)
			#print(employment.text)
			output_employment_list.append(employment.text)
			#jobs = jobtable.find_elements_by_css_selector('th.tableCondition__head')
			bodys = jobtable.find_elements_by_css_selector('td.tableCondition__body')
			# for job, body in zip(jobs, bodys):
			# 	print(job.text)
			# 	print(body.text)
			output_jobtable_job_list.append(bodys[0].text)
			output_jobtable_user_list.append(bodys[1].text)
			output_jobtable_place_list.append(bodys[2].text)
			output_jobtable_cost_list.append(bodys[3].text)
			#output_jobtable_firstcost_list.append(bodys[4]) #初年度年収を表示していない場合あり
			#print(updata.find_element_by_tag_name('span').text)
			output_updata_list.append(updata.find_element_by_tag_name('span').text)

			# 配列からでも取得可能
			# for jobtable in jobtable_list:
			# 	jobs = jobtable.find_elements_by_css_selector('th.tableCondition__head')
			# 	bodys = jobtable.find_elements_by_css_selector('td.tableCondition__body')
			# 	print(jobs[0].text)
			# 	print(bodys[0].text)
			# 	print(jobs[1].text)
			# 	print(bodys[1].text)
			# 	print(jobs[2].text)
			# 	print(bodys[2].text)
		
		log(f'{page_no} ページ目取得終了です')

		try:
			driver.find_element_by_class_name('iconFont--arrowLeft').click()
		except:
			log('最終ページのため、全取得完了')
			break

	df = pandas.DataFrame({
		"企業名":output_company_list,
		"キャッチコピー":output_title_list,
		"ステータス":output_employment_list,
		"仕事内容":output_jobtable_job_list,
		"対象となる方":output_jobtable_user_list,
		"勤務地":output_jobtable_place_list,
		"給与":output_jobtable_cost_list,
		#"初年度年収":output_jobtable_firstcost_list,
		"情報更新日":output_updata_list
	})
	df.to_csv(f'求人一覧_{search_keyword}_{FILENAME_DATETIME}.csv')
	driver.quit()

def input_key():
	key_word = input('検索するキーワードを入力してください：')
	return key_word

if __name__ == '__main__':
	scraping()
	