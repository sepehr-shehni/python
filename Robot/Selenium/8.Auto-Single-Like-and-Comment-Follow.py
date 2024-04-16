from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from colorama import Fore , Style
from password import username , password
import random
import os
import time

page = input("Please Enter Your Instagram Page :").split(' ')
comments = ['Best','Great']
addresss = os.path.abspath(__file__)
addresss = os.path.dirname(addresss)
addresss = os.path.join(addresss , 'chromedriver.exe')

driver = webdriver.Chrome(executable_path=addresss)
driver.maximize_window()
driver.get('https://instagram.com')
time.sleep(2)
#Cookie Accept
try:
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]').click()
except:
    pass
usr = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')))
usr.send_keys(username)
pas = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
pas.send_keys(password + Keys.ENTER)
time.sleep(3)

for i in page:
    if '#' == i[0]:
        driver.get(f'https://instagram.com/explore/tags/{i[1:]}/')
        time.sleep(3)
        post = driver.find_element_by_class_name('_9AhH0').click()
        time.sleep(3)
        like = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
        time.sleep(2)
        comment = random.choice(comments)
        time.sleep(2)
        #Comment Button
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[2]/button').click()
        time.sleep(2)
        #Post Text Input
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(comment)
        #Post Button
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button[2]').click()
        time.sleep(2)
        # Follow
        # Result = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/header/div[2]/div/button')
        # if Result.text == 'Follow':
        #     Result.click()
    else:
        driver.get(f'https://instagram.com/{i}/')
        time.sleep(3)