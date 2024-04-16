from selenium import webdriver
import os
from time import sleep

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IE_DIR = os.path.join(BASE_DIR, 'geckodriver')
IG_URL = 'http://instagram.com'

class BOT:
	def __init__(self):
		self.driver = webdriver.Firefox(executable_path=IE_DIR)

	def go_Signup_page(self):
		self.driver.get(IG_URL)
		sleep(1)
		self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[2]/div/p/a/span').click()



if __name__ == '__main__':
	bt = BOT()
	bt.go_Signup_page()