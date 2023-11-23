from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("./msedgedriver.exe")
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(service=service, options=options)

minPrice = 1000
maxPrice = 2000
facebook_url = 'https://www.facebook.com/marketplace/category/propertyrentals?minPrice='+str(minPrice)+'&maxPrice='+str(maxPrice)+'&exact=false'

xpat1 = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div[3]/div[2]/div[2]/div/div[2]/div['
xpat2 = ']/div/div/span/div/div/a'


driver.get(facebook_url)
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('xwang174@lakeheadu.ca')
driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys('craft071611')
driver.find_element(By.XPATH, '//*[@id="loginbutton"]').click()


time.sleep(5)

_ = 0
while True:
    _ = _ + 1
    try:
        print(driver.find_element(By.XPATH, xpat1+str(_)+xpat2).get_attribute('href'))
    except:
        break

driver.close()

