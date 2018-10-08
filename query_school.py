# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 18:52:36 2018

@author: mengh
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time

def tryclick(driver, selector, count=0): ##保護機制，以防無法定味道還沒渲染出來的元素
    try:
        elem = driver.find_element_by_css_selector(selector)
        # elem = driver.find_element_by_xpath(Xpath)  # 如果你想透過Xpath定位元素
        elem.click() # 點擊定位到的元素
    except:
        time.sleep(2)
        count+=1
        if(count <2):
            tryclick(driver, selector,count)
        else:
            print("cannot locate element" + selector)

def input_text(driver, selector, text, count=0):
    try:
        elem = driver.find_element_by_css_selector(selector)
        # elem = driver.find_element_by_xpath(Xpath)  # 如果你想透過Xpath定位元素
        elem.click() # 點擊定位到的元素
        elem.send_keys(text) # 點擊定位到的元素
    except:
        time.sleep(2)
        count+=1
        if(count <2):
            tryclick(driver, selector,count)
        else:
            print("cannot locate element" + selector)
            
def query_school(address):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    #driver = webdriver.Chrome(options=option)
    chromedriver = "C:\\Users\\mengh\\Documents\\python\\chromedriver"
    driver = webdriver.Chrome(chromedriver, options=option) # 如果你沒有把webdriver放在同一個資料夾中，必須指定位置給他
    driver.get("https://www.tp.edu.tw/neighbor/html/")
    input_text(driver, "#k2", address) # 設定成中文
    
    tryclick(driver, "#searchBtn2") # 點擊「檢索」按鍵
    
    
    time.sleep(4) # 等待javascript渲染出來，當然這個部分還有更進階的作法，關鍵字是implicit wait, explicit wait，有興趣可以自己去找
    html = driver.page_source # 取得html文字
    driver.close()  # 關掉Driver打開的瀏覽器
    print(html)
    
    page = BeautifulSoup(html, "html.parser")
    result = page.findAll("div", {"id": "content"})
    print(result)
    school = ', '.join([i.getText() for i in result[0].findAll("a", href=True) if '小' in i.getText() or '中' in i.getText()])
    return school


if __name__ == '__main__':
    print(query_school("南京東路2段196號7樓"))