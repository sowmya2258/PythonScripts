from selenium import webdriver
from bs4 import BeautifulSoup
import requests

url = 'https://www.imdb.com/gallery/rg1624939264?ref_=nv_ph_lp'

driver = webdriver.Chrome(executable_path = r'C:\Users\exe files\chromedriver.exe')

driver.get(url)

soup = BeautifulSoup(driver.page_source,'lxml')

div = soup.find('div',class_='media_index_thumb_list')

a = div.find ('a')

print ('https://www.imdb.com' + a['href'])

url = 'http://www.imdb.com' + a['href']

driver.get(url)

soup = BeautifulSoup(driver.page_source,'lxml')

all_div = soup.find_all('div',class_='pswp__zoom-wrap')

all_img = all_div[1].find_all('img')

print  (all_img[1]['src'])

f = open ('latestimg.jpg','wb')
f.write(requests.get(all_img[1]['src']).content)
f.close()
f.quit()