from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import csv
from selenium import webdriver


driver = webdriver.Chrome('/Users/sarah/Documents/python/scraping_project/chromedriver')
driver.get('https://www.usa.gov/federal-agencies/')
html = driver.page_source

bs = BeautifulSoup(html, 'html.parser')

agency_list = []

def get_agencies(html, bs):
    agency_list = []
    for ul in bs.find_all('ul', {'class':'one_column_bullet'}):
        for li in ul.find_all('li'):
            a = li.find('a')
            if a.has_attr('href'):
                agency_list.append(a['href'])
    return agency_list

agency = get_agencies(html, bs)
print(agency)
