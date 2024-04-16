from selenium import webdriver
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IE_DIR = os.path.join(BASE_DIR, 'IEDriverServer.exe')

class BOT:
	def __init__(self):
		self.driver = webdriver.Ie(executable_path=IE_DIR)


if __name__ == '__main__':
	bt = BOT()