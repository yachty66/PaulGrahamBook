'''
- Notes:
    - i have lots of requests and need to create lots of soup with these urls
    - i collect requests in list
    - how do i deal with headers. in step where i get comp i also collect header in sperate var and add to seperate list
    - wjhen looping i always first write headline and then comp - need to check that headline is fat and has line breaks
    - need to remove everything from content from <b>Notes</b> on 
    
    - need to remove notes and find a better pdf conversion tool to avoid â€
    - â€ appears for —. Can i replace â€ with —?
    - now everything should work
    - i should do it like that: if notes or note appears remove everything after that otherwise do not remobe anything
    
    
    - if Notes is in lis of tags remove everything after that, if note is in list of tags remove everything after that, if thanks is in list of tags remove everything after that
    - still getting no desired result. need to check reoving after notes. It exist currentl posts which are just added to pdf         


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
    return links


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
    return headlines


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
        check = False
        getUrl = requests.get(link)
        soup = BeautifulSoup(getUrl.content, 'html.parser')
        con = soup.find_all('font', face="verdana", size="2")[0]
        all=con.find_all('b')
        #if link == 'http://www.paulgraham.com/13sentences.html':
        #    print(all)
        #only if all is not empty
        if all:
            for i in all:
                if i.text.strip() == 'Notes':
                    for j in i.find_all_next():
                        j.extract()
                    for j in i.find_all_next(string=True):
                        j.extract()
                    con.find_all('b')[-1].extract()
                    content.append(con.prettify())
                    '''for j in i.find_all_next():
                        j.extract()
                    for j in i.find_all_next(string=True):
                        j.extract()
                    con.find_all('b')[-1].extract()'''
                elif i.text.strip() == 'Note':
                    for j in i.find_all_next():
                        j.extract()
                    for j in i.find_all_next(string=True):
                        j.extract()
                    con.find_all('b')[-1].extract()
                    content.append(con.prettify())
                elif i.text.strip() == 'Thanks':
                    for j in i.find_all_next():
                        j.extract()
                    for j in i.find_all_next(string=True):
                        j.extract()
                    #print(con.find_all('b'))
                    try:
                        con.find_all('b')[-1].extract()
                        content.append(con.prettify())
                    except IndexError:
                        pass
        else:
            content.append(con.prettify())
                
                #pos = all.index(i)
                #check = True
                #print(con.find_all("b"))
                #print(con.find_all("b")[pos])

        '''if check:   
            #if pos > 3:
             #   print(i.find_all_next())
            #only reason why 
            for i in con.find_all("b")[pos]:
                for j in i.find_all_next():
                    j.extract()
                for j in i.find_all_next(string=True):
                    j.extract()
            con.find_all('b')[-1].extract()
        elif len(con.find_all('b')) > 0 and check == False:
            for i in con.find_all("b")[0]:
                print(i)
                print(link)
                for j in i.find_all_next():
                    j.extract()
                for j in i.find_all_next(string=True):
                    j.extract()
            con.find_all('b')[-1].extract()'''
        #content.append(con.prettify())
    return content


def writeToHtml(headlines, content): 
    with open('book.html', 'w') as f:
        #write on top of book.html content from head.html
        f.write("<head><meta charset='utf-8'></head>")
        for headline, con in zip(headlines, content):
            f.write(headline)
            f.write(con)
            f.write('<br><br>')


def hmtlToPdf():
    import pdfkit
    #before converting add <meta charset="utf-8"> to html head
    '''with open('book.html', 'r') as f:
        html = f.read()
        html = html.replace('<head>', '<head><meta charset="utf-8">')
        with open('book.html', 'w') as f:
            f.write(html)'''
    pdfkit.from_file('book.html', 'new.pdf')


def test(): 
    openHtml = open('test.html', 'r')
    soup = BeautifulSoup(openHtml, 'html.parser')
    con = soup.find_all('font', face="verdana", size="2")[0]
    all=con.find_all('b')
    if all:
        for i in all:
            if i.text.strip() == 'Notes':
                for j in i.find_all_next():
                    j.extract()
                for j in i.find_all_next(string=True):
                    j.extract()
                con.find_all('b')[-1].extract()
                print(con.prettify())        



    
    

if __name__ == '__main__':
    # getLinks()
    # print(getHeadlines())
    # print(getContent(getLinks()))
    writeToHtml(getHeadlines(), getContent(getLinks()))
    hmtlToPdf()
    #getContent("test")
    #test()
    # this works i should remove the notes section
