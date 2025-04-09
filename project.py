from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

driver = webdriver.Firefox()

driver.get('https://inshorts.com/en/read')
time.sleep(2)
d= {}
i = 0
for _ in range(1,10):
    driver.execute_script('window.scrollBy(0,10000);')
    link = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME,'QMXJlc3R5MMJjDGSV4Jd')))
    link.click()
    time.sleep(1)
    
    
soup = BeautifulSoup(driver.page_source,'lxml')

details = soup.find_all('div','VdsPqrmJYY7F2MNUKOwQ')
for detail in details:
    title = detail.find('span','S2DdZEgzkqC9bYeTJUGw').text
    by = detail.find('span','author').text
    times = detail.find('div','njwxOAklpbTYvII3gDje').find_all('span')[2].text
    date = detail.find('span','date').text
    data = detail.find('div','Hxtmf9GvkV8Ti6V0GUSn').text
    
    d[i] = [title,by,times,date,data]
    i += 1
driver.quit()

with open('inshorts_project/result.csv','w',encoding='utf-8',newline='') as file:
    import csv
    writer = csv.writer(file)
    writer.writerow(['title','Author','time','date','details'])
    for i in range(len(d)):
        writer.writerow(d[i])