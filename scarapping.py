from flask import Flask,render_template, request, jsonify
from bs4 import BeautifulSoup as bs
from urllib. request import urlopen as urReq
import requests
flipcart_url = "https://www.flipkart.com/search?q="+"iphone11"
respone_website = urReq(flipcart_url)
data_flipcart = respone_website.read()
beautiful_html = bs(data_flipcart, "html.parser")
bigbox = beautiful_html.find_all("div", {"class":"_1AtVbE col-12-12"})
link_url =bigbox[0].div.div.div.a['href']
product6 = "https://www.flipkart.com"+ link_url
product66 = requests.get(product6)
product66.encoding = 'utf-8'
product66_link = bs(product66.text, "html.parser")
print(product66_link)
