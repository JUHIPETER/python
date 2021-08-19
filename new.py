import selenium
from selenium import webdriver
from selenium.common.exceptions import InvalidSessionIdException
import pandas as pd
import time
import  os
driverPath = r"C:\Users\Merit\PycharmProjects\chrome\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(executable_path = driverPath)
driver.maximize_window()
driver.get("https://www.cricbuzz.com/cricket-match/live-scores")
driver.find_element_by_xpath("//a[contains(text(),'Teams')]").click()
driver.find_element_by_xpath("//a[contains(text(),'International')]").click()
match = driver.find_elements_by_xpath("//h1[contains(text(),'Cricket Teams')]//following::h2")
l=[]
for i in match:
    l.append(i.text)
T1= driver.find_elements_by_xpath("//div[contains(@class,'cb-col cb-col-25')]")
for i,j in zip(T1,l):
    with open(j+".png",'wb') as file:
         file.write(i.screenshot_as_png)
         time.sleep(2)
         #driver.close()


         os.chdir(r'C:\Users\Merit\PycharmProjects\pythonProject\image')