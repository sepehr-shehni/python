from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from password import username , password

page = input("Please Enter Your Instagram Page :").split(' ')
addresss = os.path.abspath(__file__)
addresss = os.path.dirname(addresss)
addresss = os.path.join(addresss , 'geckodriver.exe')

driver = webdriver.Firefox(executable_path=addresss)
driver.get('https://instagram.com')

usr = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')))
usr.send_keys(username)
pas = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
pas.send_keys(password + Keys.ENTER)

for i in page:
    if '#' == i[0]:
        driver.get(f'https://www.instagram.com/explore/tags/{i[1:]}/')
    else:
        driver.get(f'https://www.instagram.com/{i}/')


