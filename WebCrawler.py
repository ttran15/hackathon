from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time
import json

service = Service("./msedgedriver.exe")
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(service=service, options=options)
driver.get('https://www.facebook.com/marketplace/category/propertyrentals')
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('xwang174@lakeheadu.ca')
driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys('craft071611')
driver.find_element(By.XPATH, '//*[@id="loginbutton"]').click()

canada_city = pd.read_csv("canadacity.csv")
dic_url = {}
for province in list(canada_city["province"]):
    dic_url[province] = {}
    a = canada_city[canada_city["province"] == province]
    for city in list(a["city"]):
        dic_url[province][city] = []
    

for index, row in canada_city.iterrows():
    province = row['province']
    city = row['city']
    lat = row['lat']
    long = row['long']
    facebook_url = "https://www.facebook.com/marketplace/category/propertyrentals/?exact=false&latitude=" + str(lat) + "&longitude=" + str(long) + "&radius=1"

    xpat1 = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div[3]/div[2]/div[2]/div/div[2]/div['
    xpat2 = ']/div/div/span/div/div/a'

    driver.get(facebook_url)
    time.sleep(1)

    _ = 0
    while True:
        _ = _ + 1
        try:
            # print(driver.find_element(By.XPATH, xpat1+str(_)+xpat2).get_attribute('href'))
            dic_url[province][city].append(driver.find_element(By.XPATH, xpat1+str(_)+xpat2).get_attribute('href'))
        except:
            break

    #break

# save dictionary
with open("dic_url.json", "w") as fp:
    json.dump(dic_url , fp)

driver.close()
