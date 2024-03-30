from bs4 import BeautifulSoup as BS
import requests
def unite1(nu):
    un = ""
    for i in nu:
        un += i + "*"
    return un
def unite2(ne):
    en = []
    for i in ne:
        en = en + i
    return en
import codecs
import re
divs = []
#https://brobank.ru/banki/tinkoff/comments/comment-page-2/#comments
for num_page in range(1, 13):
    url = 'https://brobank.ru/banki/tinkoff/comments/comment-page-' + str(num_page) + '/#comments'
    #url = 'https://bankiros.ru/bank/tcs/otzyvy?limit=100'
    page = requests.get(url)
    print(page.status_code)
    html_page = BS(page.content, "html.parser")
    #div = html_page.find_all("p", attrs = {"class": "xxx-reviews-card__content"})
    div = html_page.find_all("section", attrs = {"class": "comment-content comment"})
    div1 = []
    for i in div:
        y = i.text
        div1 += [y]
    divs += [div1]
file = open('save1_utf-8.txt', 'w', encoding='utf-8')
file.write(unite1(unite2(divs)))