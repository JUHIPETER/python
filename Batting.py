import selenium
from selenium import webdriver
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from selenium.webdriver.support.ui import Select
import time
import  os
driverPath = r"C:\Users\Merit\PycharmProjects\chrome\chromedriver_win32 (1)\chromedriver.exe"
driver = webdriver.Chrome(executable_path = driverPath)
driver.get("https://www.cricbuzz.com/")
print(driver.title)
print(driver.current_url)
driver.maximize_window()

MatchType = ['Test', 'ODI', 'T20I']

driver.find_element_by_xpath("//div[@id='rankingDropDown']").click()
time.sleep(2)
driver.find_element_by_xpath("//a[@id='batsmen-tab']").click()
time.sleep(2)
driver.find_elements_by_xpath("//a[@id='batsmen-tab']//following::a[contains(@class,'cb-nav-pill-1 cb-font-12')]")
l=[]
position=[]
player=[]
ranking=[]
table=driver.find_elements_by_xpath('//*[@id="page-wrapper"]/div[3]/div[2]/div/div/div[1]/div') 
headers=table[0].text
li=headers.split("\n")
for i in table[1:]:
    content=i.text
    pl=content.split("\n")
    position.append(pl[0])
    player.append(pl[2])
    ranking.append(pl[4])
df=pd.DataFrame({li[0]:position,li[1]:player,li[2]:ranking})
writer =pd.ExcelWriter("Batting.xlsx", engine="xlsxwriter")
df.to_excel(writer,'Sheet1',index=False)
writer.save()
driver.close()


