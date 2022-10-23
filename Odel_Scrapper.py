#import libraries
import requests
from bs4 import BeautifulSoup
import lxml
from xlwt import *

#workbook defining
workbook = Workbook(encoding = 'utf-8')
table = workbook.add_sheet('data')

#creation of headers
table.write(0, 0, 'Product Number')
table.write(0, 1, 'Product Name')
table.write(0, 2, 'New Price')
table.write(0, 3, 'Old Price')
table.write(0, 4, 'Discount')
line = 1

#define the URL  and the header
url  = "https://odel.lk/deal-products"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}

#get the url
f = requests.get(url, headers = headers)

#parsing
soup = BeautifulSoup(f.content,'lxml')
#print(soup)

#extract information
products = soup.find('div',{'class':'container'}).find_all('div',{'class':'col-sm-6 col-md-4 col-lg-3 p-b-35 product-tile-search'})
#print(products)

num = 0
product_list = []

for product in products:
  num += 1
  #print(num)

  productName = product.find('div',{'class':'block2'}).find('a',{'class':'stext-104 cl4 hov-cl1 trans-04 js-name-b2 p-b-6'}).string.strip()
  #print(productName)

  newPrice = product.find('div',{'class':'block2'}).find('span',{'class':'stext-105 cl3'}).string.strip()
  #print(newPrice)

  oldPrice = product.find('div',{'class':'block2'}).find('del').string.strip()
  #print(oldPrice)

  discount = product.find('div',{'class':'block2'}).find('div',{'class':'product_tag_discount'}).string.strip()
  #print(discount)

  line += 1

  table.write(line, 0, num)
  table.write(line, 1, productName)
  table.write(line, 2, newPrice)
  table.write(line, 3, oldPrice)
  table.write(line, 4, discount)

  workbook.save('odel-deal-products.xls')
