import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://arjang.ac.ir/calendar/full"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
captions = soup.find_all('caption')
caption_texts = [caption.get_text(strip=True) for caption in captions]
df = pd.DataFrame(caption_texts, columns=['Caption'])
excel_file_path = r"D:\classes.xlsx"
df.to_excel(excel_file_path, index=False)
print("Captions scraped and saved to", excel_file_path)
