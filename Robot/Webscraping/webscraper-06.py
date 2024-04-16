#Finding Elements by ID
import requests 
from bs4 import BeautifulSoup 


# Making a GET request 
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/') 

# Parsing the HTML 
soup = BeautifulSoup(r.content, 'html.parser') 

# Finding by id 
s = soup.find('div', id= 'main') 

# Getting the leftbar 
leftbar = s.find('ul', class_='leftBarList') 

# All the li under the above ul 
content = leftbar.find_all('li') 

print(content)
