from bs4 import BeautifulSoup
import requests


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
    content = []
    for link in links:
        check = False
        getUrl = requests.get(link)
        soup = BeautifulSoup(getUrl.content, 'html.parser')
        con = soup.find_all('font', face="verdana", size="2")[0]
        all = con.find_all('b')
        if all:
            for i in all:
                if i.text.strip() == 'Notes':
                    for j in i.find_all_next():
                        j.extract()
                    for j in i.find_all_next(string=True):
                        j.extract()
                    con.find_all('b')[-1].extract()
                    content.append(con.prettify())
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
                    try:
                        con.find_all('b')[-1].extract()
                        content.append(con.prettify())
                    except IndexError:
                        pass
        else:
            content.append(con.prettify())
    return content


def writeToHtml(headlines, content):
    with open('book.html', 'w') as f:
        f.write("<head><meta charset='utf-8'></head>")
        for headline, con in zip(headlines, content):
            f.write(headline)
            f.write(con)
            f.write('<br><br>')


def hmtlToPdf():
    import pdfkit
    pdfkit.from_file('book.html', 'PaulGrahamEssayBook.pdf')


if __name__ == '__main__':
    writeToHtml(getHeadlines(), getContent(getLinks()))
    hmtlToPdf()
