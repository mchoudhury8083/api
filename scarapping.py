from flask import Flask,render_template, request, jsonify
from bs4 import BeautifulSoup as bs
from urllib. request import urlopen as urReq
flipcart_url = "https://www.flipkart.com/search?q="+"iphone11"
respone_website = urReq(flipcart_url)
data_flipcart = respone_website.read()
beautiful_html = bs(data_flipcart, "html.parser")
print(beautiful_html)
