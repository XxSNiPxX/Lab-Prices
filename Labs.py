# -*- coding: utf-8 -*-
"""
Created on Tue May 22 10:19:47 2018

@author: Rishabh
"""
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
data=None

links=['shree-krishna-diagnostic-laboratory-204']
for x in links:
   driver= webdriver.Chrome("C:/Users/User/Downloads\chromedriver_win32/chromedriver.exe")
   price_list_net=[]
   price_list_mrp=[]
   test_name_list=[]
   
   
   driver.get('https://www.1mg.com/labs/hyderabad/diagnostic-centers/{}'.format(x))
   time.sleep(3)
   try:
       while True:
            button=driver.find_element_by_css_selector('#body-container > div > div.row.style__lab-page___2tRYJ > div.col-lg-8.col-xs-12.style__desktop-view___1BKQw > div.style__lab-cards-wrapper___2gs3Q > div.style__upper-view-more___2edvG > div > div > div')
            button.click()
            time.sleep(0.75)
        
   except NoSuchElementException as e:
         pass
   try:
       for i in range(1,1000):
   #price=driver.find_element_by_css_selector('#body-container > div > div.row.style__lab-page___2tRYJ > div.col-lg-8.col-xs-12.style__desktop-view___1BKQw > div.style__lab-cards-wrapper___2gs3Q > div.row.style__cards-margin___1Cat_ > div:nth-child(1) > div > a > div > div.col-lg-6.col-xs-6.SkuCard__right-align___1D-dj > div > div > div:nth-child({}) > div > span.SkuCard__mrp___2qdax'.format(i))
           test_name=driver.find_element_by_css_selector('#body-container > div > div.row.style__lab-page___2tRYJ > div.col-lg-8.col-xs-12.style__desktop-view___1BKQw > div.style__lab-cards-wrapper___2gs3Q > div > div:nth-child({}) > div > a > div > div:nth-child(1) > h3'.format(i))
           test_name_list.append(test_name.text) 
           #print(test_name)
                                      
           try:                                              
               test_price_net=driver.find_element_by_css_selector('#body-container > div > div.row.style__lab-page___2tRYJ > div.col-lg-8.col-xs-12.style__desktop-view___1BKQw > div.style__lab-cards-wrapper___2gs3Q > div > div:nth-child({}) > div > a > div > div.col-lg-6.col-xs-6.SkuCard__right-align___1D-dj > div > div > div:nth-child(1) > div > span.SkuCard__mrp___2qdax'.format(i))
               price_list_net.append(test_price_net.text) 
               #print(test_price)
           except NoSuchElementException as e:
               test_price_net='Not Found'
               price_list_net.append(test_price_net)
           try:
               
               test_price_mrp=driver.find_element_by_xpath('//*[@id="body-container"]/div/div[2]/div[2]/div[1]/div[1]/div[{}]/div/a/div/div[2]/div/div/div[1]/div/span[1]/strike/span'.format(i))
               price_list_mrp.append(test_price_mrp.text)
           except NoSuchElementException as e:
               test_price_mrp='Same as Net'
               price_list_mrp.append(test_price_mrp)    
                     
           data=pd.DataFrame({'Test':test_name_list,'Net Price':price_list_net,'MRP Price':price_list_mrp})
   except NoSuchElementException as e:
          pass
   
   writer = pd.ExcelWriter('Lab_Prices_{}.xlsx'.format(x), engine='xlsxwriter')
   data.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
   writer.save()
   driver.close()
   time.sleep(1)
   

   


   
   #body-container > div > div.row.style__lab-page___2tRYJ > div.col-lg-8.col-xs-12.style__desktop-view___1BKQw > div.style__lab-cards-wrapper___2gs3Q > div.style__upper-view-more___2edvG > div > div > div > div
   
   #body-container > div > div > div.col-lg-8.col-xs-12.style__desktop-view___1BKQw > div.style__lab-cards-wrapper___2gs3Q > div.row.style__cards-margin___1Cat_ > div:nth-child(1) > div