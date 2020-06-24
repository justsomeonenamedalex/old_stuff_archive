import requests
from bs4 import BeautifulSoup
import re
request = input

def search(term):
    term_list = []
    for i in term:
        if i != " ":
            term_list.append(i)
        else:
            term_list.append("%20")

    url_term = "".join(term_list)
    url_2 = f"http://www.scp-wiki.net/search:site/q/{url_term}"
    page_2 = requests.get(url_2)
    soup_2 = BeautifulSoup(page_2.content, 'html.parser')
    results = soup_2.find(class_="item")
    for link in results.findAll('a', attrs={'href': re.compile("^http://")}):
        new_page = link.get('href')
    print("ARTICLE FOUND")
    return new_page    

def get_article(URL):
    print("FETCHING ARTICLE")
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='page-content')

    result = results.findAll('p')

    document_lines = []

    for i in result:
        document_lines.append(i.text)

    document_lines.remove(document_lines[-1])
    return document_lines

while True:
    request = input("ENTER SCP NUMBER: ")
    formatted_url = f"http://www.scp-wiki.net/{request}"
    document = get_article(formatted_url)

    if document[0] == "Did you get feedback first?":
        print("SEARCHING DATABASE")
        new_url = search(request)
        for line in get_article(new_url):
            print(line)
    else:
        for line in document:
            print(line)


