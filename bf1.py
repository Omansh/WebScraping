# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 17:21:13 2019

@author: Omansh.Singh
"""

import bs4 as bs
import urllib.request
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


#sauce=urllib.request.urlopen("putlink").read()
#soup=bs.BeautifulSoup(sauce,'lxml')
#print(soup.title.text)
#
##for paragraph in soup.find_all('p'):
##    print(paragraph.text)
    
my_url="https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"
uClient = uReq(my_url)#Opening the connections & Grabbing the page
page_html =uClient.read()
uClient.close()
#print(page_html)

#Html Parsing 
page_soup = soup(page_html,"html.parser")


#Grab each product
containers = page_soup.findAll("div",{"class":"item-container"})


filename='products.csv'
f = open(filename, "w")

headers="brand, product_name, shipping\n"

f.write(headers)


#container = containers[0]
for container in containers:
    brand = container.a.img['title']
    
    title_container = container.findAll("a",{'class':'item-title'})
    product_name = title_container[0].text
    
    shiping_container = container.findAll('li',{'class':'price-ship'})
    shipping = shiping_container[0].text.strip()
    
    print("brand: " +brand)
    print("Product name: "+product_name)
    print("Shipping: "+shipping)
    
    f.write(brand.replace(",","|") + "," + product_name.replace(",","|") + "," + shipping.replace(",","|")+"\n") 
f.close()
    

    
    
    