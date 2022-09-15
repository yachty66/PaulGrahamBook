'''
- Notes:
    - i have lots of requests and need to create lots of soup with these urls
    - i collect requests in list
    - how do i deal with headers. in step where i get comp i also collect header in sperate var and add to seperate list
    - wjhen looping i always first write headline and then comp - need to check that headline is fat and has line breaks
    - need to remove everything from content from <b>Notes</b> on 
    
    - need to remove notes and find a better pdf conversion tool to avoid â€



- [x] make a list with all links
- [x] make list for headlines and comp
- [x] iter to get make soup objects from links
- [x] in same iter get comp of soup object and headline and append to respective lists
- [x] keep attention that headline contains line breaks and is fat
- [ ] write everything to html
- [ ] convert html to pdf
- [ ] next steps
'''
from cgitb import html
from os import remove
from pydoc import source_synopsis
from re import S
from turtle import position
from bs4 import BeautifulSoup
import requests


# get all links
def getLinks():
    getUrl = requests.get('http://www.paulgraham.com/articles.html')
    soup = BeautifulSoup(getUrl.content, 'html.parser')
    allLinks = soup.find_all('a')[4:]
    href = [link.get('href') for link in allLinks]
    href = [link for link in href if link.endswith('html')]
    href = href[:-1]
    links = ['http://www.paulgraham.com/' + link for link in href]
    return links[:5]


def getHeadlines():
    getUrl = requests.get('http://www.paulgraham.com/articles.html')
    soup = BeautifulSoup(getUrl.content, 'html.parser')
    allLinks = soup.find_all('a')[4:]
    href = [link.get('href') for link in allLinks]
    href = [link for link in href if link.endswith('html')]
    href = href[:-1]
    headlines = [link.text for link in allLinks]
    headlines = [f'<b>{headline}</b><br>' for headline in headlines]
    headlines = headlines[:-1]
    return headlines[:5]


def getContent(links):
    '''getUrl = requests.get("http://www.paulgraham.com/fn.html")
    soup = BeautifulSoup(getUrl.content, 'html.parser')
    con = soup.find_all('font', face="verdana", size="2")[0]
    all=con.find_all('b')
    for i in all:
        if i.text.strip() == 'Notes':
            pos = all.index(i)
    for i in con.find_all("b")[pos]:
        for j in i.find_all_next():
            j.extract()
    con.find_all('b')[-1].extract()'''
    #print(soup.prettify())
    #print(con.prettify())
    #content.append(con.prettify())
    #return content[:5]
    content = []
    for link in links:
        getUrl = requests.get(link)
        soup = BeautifulSoup(getUrl.content, 'html.parser')
        con = soup.find_all('font', face="verdana", size="2")[0]
        all=con.find_all('b')
        for i in all:
            if i.text.strip() == 'Notes':
                pos = all.index(i)
        for i in con.find_all("b")[pos]:
            for j in i.find_all_next():
                j.extract()
        con.find_all('b')[-1].extract()
        content.append(con.prettify())
    return content[:5]


def writeToHtml(headlines, content):
    with open('book.html', 'w') as f:
        for headline, con in zip(headlines, content):
            f.write(headline)
            f.write(con)
            f.write('<br><br>')


def hmtlToPdf():
    import pdfkit
    pdfkit.from_file('book.html', 'new.pdf')


def test(): 
    openHtml = open('test.html', 'r')
    soup = BeautifulSoup(openHtml, 'html.parser')
    #find all b tags
    all=soup.find_all('b')
    #iter over all b tags 
    for i in all:
        #if text is notes store index
        if i.text.strip() == 'Notes':
            pos = all.index(i)
    #for in in notes tag 
    for i in soup.find_all("b")[pos]:
        #this should contain the nerd text --> this contains actually all the text already - so the result should be text with stop at notes
        #print(i.find_all_next())
        for j in i.find_all_next(string=True):
            j.extract()
        for j in i.find_all_next():
            j.extract()
    #print adjusted soup
    
    soup.find_all('b')[-1].extract()
    print(soup.prettify())        



    
    

if __name__ == '__main__':
    # getLinks()
    # print(getHeadlines())
    # print(getContent(getLinks()))
    #writeToHtml(getHeadlines(), getContent(getLinks()))
    #hmtlToPdf()
    #getContent("test")
    test()
    # this works i should remove the notes section
