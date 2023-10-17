import requests
from bs4 import BeautifulSoup

with open('index.html', 'r') as f:
   html_doc = f.read()
   
soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())
# print(soup.title, type(soup.title.string))
# print(soup.title.name)

con = soup.find(class_ = "container")
con.name = 'span'
con['class'] = "myclass class1"
con.string = 'this is changed'
print(con)