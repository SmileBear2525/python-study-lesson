import time

from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://www.google.com/?hl=ja")
print(driver.title)
search = driver.find_element_by_name('q')
search.send_keys('スクレイピング')
search.submit()
time.sleep(3) #3s待機

class_name = 'LC20lb'
class_elems = driver.find_elements_by_class_name(class_name)
for elem in class_elems:
	print(elem.text)

tags = driver.find_elements_by_tag_name('span')
for tag in tags:
	print('-----')
	print(tag.get_attribute('innerHTML'))

driver.quit()
