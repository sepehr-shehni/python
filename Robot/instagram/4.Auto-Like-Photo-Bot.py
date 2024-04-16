from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
from time import sleep



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IE_DIR = os.path.join(BASE_DIR, 'geckodriver')
IG_URL = 'http://instagram.com'

class BOT:

	def __init__(self):
		self.driver = webdriver.Firefox(executable_path=IE_DIR)


	def go_login_page(self):
		self.driver.get(IG_URL)
		sleep(1)


	def login(self):
		un_id = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.-MzZI:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')))
		un_id.click()
		un_id.send_keys("your username")

		pw_id = self.driver.find_element_by_css_selector('div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
		pw_id.click()
		pw_id.send_keys("your password")

		btn = self.driver.find_element_by_css_selector('.bkEs3')
		btn.click()
		sleep(5)

		self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
		sleep(1)

		self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
		sleep(1)


	def like_photo(self, hashtag, amount):
		hashtag_url = 'https://www.instagram.com/explore/tags/' + hashtag
		self.driver.get(hashtag_url)
		sleep(3)
		self.driver.find_element_by_class_name('Nnq7C').click()

		i = 1
		while i <= amount:
			sleep(3)
			btn_like = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button')
			btn_like.click()
			sleep(3)
			self.driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
			i += 1




if __name__ == '__main__':
	bt = BOT()
	bt.go_login_page()
	bt.login()
	bt.like_photo('pythonprogramming', 3)