# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 13:07:18 2019

@author: Omansh.Singh
"""

import bs4 as bs
import urllib.request
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re


#sauce=urllib.request.urlopen("putlink").read()
#soup=bs.BeautifulSoup(sauce,'lxml')
#print(soup.title.text)
#
##for paragraph in soup.find_all('p'):
##    print(paragraph.text)
    
my_url="https://www.flipkart.com/redmi-7a-matte-blue-32-gb/product-reviews/itmfhz4cztznu8kk?pid=MOBFHZ4BZW2GM6UH"
uClient = uReq(my_url)#Opening the connections & Grabbing the page
page_html =uClient.read()
uClient.close() #Closing the connection.
#print(page_html)

#Html Parsing 
page_soup = soup(page_html,"html.parser")


#Grab each review
#containers = page_soup.findAll("div",{"class":"qwjRop"})
#container.div.div.text   #This can grab the user review text.

containers1=page_soup.findAll('div',{"class":"col _390CkK _1gY8H-"})


filename='products_review.csv'
f = open(filename, "w")

headers="user_comment, user_review\n"

f.write(headers)


##container = containers[0]
#for container in containers:
#    brand = container.a.img['title']
#    
#    title_container = container.findAll("a",{'class':'item-title'})
#    product_name = title_container[0].text
#    
#    shiping_container = container.findAll('li',{'class':'price-ship'})
#    shipping = shiping_container[0].text.strip()
#    
#    print("brand: " +brand)
#    print("Product name: "+product_name)
#    print("Shipping: "+shipping)

for container1 in containers1:
    
    comment_container = container1.findAll("p",{'class':'_2xg6Ul'})
    user_comment = comment_container[0].text
    
    
    review_container = container1.findAll("div",{'class':'qwjRop'})
    user_review = review_container[0].div.div.text
    
#    shiping_container = container.findAll('li',{'class':'price-ship'})
#    shipping = shiping_container[0].text.strip()
    
    
    user_comment=re.sub(r"\W"," ",user_comment)
    user_review=re.sub(r"\W"," ",user_review)
    
    print("User Comment : " +user_comment)
    print("User Review: "+user_review)
    
    f.write(user_comment+","+user_review+"\n") 
f.close()
    

    
    
    