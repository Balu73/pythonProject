import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.bikewale.com/royalenfield-bikes/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.text)    #  To scrap the information from the website
# Image
image = soup.findAll('div', class_="imageWrapper relative")
for i in image:
    j = i.img['src']
    print(j)