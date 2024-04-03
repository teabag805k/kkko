from bs4 import BeautifulSoup as BS
import requests
def unite1(nu):
    un = ""
    for i in nu:
        un += i + '*'
    return un
def unite3(nu):
    un = ""
    for i in nu:
        un += i
    return un
def unite2(ne):
    en = []
    for i in ne:
        en = en + i
    return en
import codecs
import re
divs = []
#num_page = 1
# url = 'https://www.banki.ru/services/responses/bank/alfabank/?page='
#https://brobank.ru/banki/tinkoff/comments/comment-page-2/#comments
#while requests.get(url + str(num_page)).status_code == 200:
for num_page in range(1):
    #url = 'https://brobank.ru/banki/tinkoff/comments/comment-page-' + str(num_page) + '/#comments'
    url = 'https://ru.myfin.by/bank/tcs/otzyvy?limit=100'
    page = requests.get(url)
    print(page.status_code)
    print(num_page)
    html_page = BS(page.content, "html.parser")
    div = html_page.find_all("div", attrs = {"class": "review-block__text"})
    div1 = []
    for i in div:
        y = i.text
        print(y)
        div1 += [y]
    divs += [div1]
for num_page in range(1, 13):
    url = 'https://brobank.ru/banki/tinkoff/comments/comment-page-' + str(num_page) + '/#comments'
    #url = 'https://ru.myfin.by/bank/tcs/otzyvy?limit=100'
    page = requests.get(url)
    print(page.status_code)
    print(num_page)
    html_page = BS(page.content, "html.parser")
    div = html_page.find_all("section", attrs = {"class": "comment-content commentt"})
    div1 = []
    for i in div:
        y = i.text
        print(y)
        div1 += [y]
    divs += [div1]
file = open('save99_utf-8.txt', 'w', encoding='utf-8')
file.write(unite1(divs[0]))
file = open('save999_utf-8.txt', 'w', encoding='utf-8')
file.write(unite1(divs[1]))