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
driver.get("https://ai.fmcsa.dot.gov/hhg/Search.asp?ads=a")
print(driver.title)
print(driver.current_url)
driver.maximize_window()

select = Select(driver.find_element_by_xpath("//label[contains(text(),'State :')]//following::select[1]"))
select.select_by_visible_text('Maryland')
driver.find_element_by_xpath("//tbody/tr[1]/td[2]/input[3]").click()

headRows = driver.find_elements_by_xpath("//tbody/tr[1]/th")
headers=[]
for a in headRows:
    headers.append(a.text)
print(headers)


company_name=[]
headquarters=[]
company_type=[]
fleet_size=[]
for i in range(2,500):
    content=driver.find_elements_by_xpath("//body[1]/table[1]/tbody[1]/tr[3]/td[1]/table[1]/tbody[1]/tr[2]/td[3]/table[1]/tbody[1]/tr[8]/td[1]/table[1]/tbody[1]/tr[%d]/td" %(i))
    l=[]
    for i in content:
        l.append(i.text)
    company_name.append(l[0])
    headquarters.append(l[1])
    company_type.append(l[2])
    fleet_size.append(l[3])

df=pd.DataFrame({headers[0]:company_name,headers[1]:headquarters,headers[2]:company_type,headers[3]:fleet_size})
writer =pd.ExcelWriter("states.xlsx", engine="xlsxwriter")
df.to_excel(writer,'Sheet1',index=False)
writer.save()
driver.close()
