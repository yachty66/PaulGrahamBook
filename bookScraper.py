'''
go and scrape all the content from http://www.paulgraham.com/articles.html to an markdown file. 
convert markdown file to pdf. I wanna scrape it with including the links.
'''
from bs4 import BeautifulSoup
import requests

#getUrl = requests.get('http://www.paulgraham.com/kate.html')
getUrl = requests.get('http://www.paulgraham.com/progbot.html')
getUrl2 = requests.get('http://www.paulgraham.com/newideas.html')

#add content of getUrl and getUrl2 together

html = [getUrl.content, getUrl2.content]

soup = BeautifulSoup(html, 'html.parser')

for i in range(len(html)):
    soup2 = BeautifulSoup(html[i+1], 'html.parser')
    soup.append(soup2)
    break



#get html from <font face="verdana" size="2"> to </font> and get the first tag 
comp = soup.find_all('font', face="verdana", size="2").prettify()


with open('test.html', 'w') as f:
    f.write("HEADLINE1\n")
    f.write(comp)


import pdfkit 
pdfkit.from_file('test.html','shaurya.pdf') # .from_url and .fro'''

#okay this is the way how it works. Instead of making hundreds of pdfs i can just make everything in one pdf
#this works but the problem is still that i do not have the headline

'''
- [ ] make a list with all links
- [ ] 
- [ ]
- [ ]
- [ ]
- [ ]
- [ ]
- [ ]
'''