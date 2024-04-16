from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from colorama import Fore , Style
from password import username , password
import os
import time
import random

#Clear Screan
os.system('cls')

Accounts = input(Fore.GREEN + 'Please Enter Page Names with Spaces :' + Fore.YELLOW).split(' ')
Number_Like = int(input(Fore.GREEN + '\n Plaese Enter Number Like :' + Fore.YELLOW))
for i in Accounts:
    if '#' in i:
        check_follow = input(Fore.GREEN + '\n Do You Want Follow Page[Y or N]: ' + Fore.GREEN)
        check_Comments = input(Fore.GREEN + 'Do You Want Comment For Page[Y or N]: ' + Fore.YELLOW )
        if check_Comments.lower() in ['y' , 'yes']:
            comments = input(Fore.GREEN + '\n Please Enter Comments and Split with "," ' + Fore.YELLOW).split(',')
        elif check_Comments.lower() in ['n' , 'no']:
            comments = False
    else:
        continue

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

for i in Accounts:
    if '#' == i[0]:
        driver.get(f'https://instagram.com/explore/tags/{i[1:]}/')
        time.sleep(3)
        post = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div[1]/div[2]').click()
        for num in range(Number_Like):
            driver.find_element_by_class_name('wpO6b  ').click()
            time.sleep(1)
            if not comments:
                pass
            else:
                comment = random.choice(comments)
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[2]/button').click() #Comment Buttom
                time.sleep(1)
                driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(comment)
                time.sleep(1)
                post_click = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button[2]')
                post_click.Keys.ENTER

            if check_follow.lower() in ['y' , 'yes']:
                result = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/header/div[2]/div/button')
                if result.text == 'Follow':
                    result.click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a') #Next Post >
    else:
        pass
else:
    Style.RESET_ALL












