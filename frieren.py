from textblob import TextBlob
import re
import nltk
#nltk.download('wordnet')
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import DictVectorizer
def uni1(nu):
    un = set()
    for i in nu:
        un = un.union(set(i[0]))
    uf = dict()
    for i in un:
        uf[i] = []
    return uf
def unite3(nu):
    un = ""
    for i in nu:
        un += i[0]
    return un
def unite(nu):
    un = ""
    for i in nu:
        un += "* " + i + "\n"
    return un
def unit(nu):
    un = []
    for i in nu:
        un += i
    return un
def une3(nu):
    un = ""
    for i in nu:
        un = un + i + ' '
    return un
def unite2(ne):
    en = []
    for i in ne:
        en = en + [i[0]]
    return en
def cerb(fer):
    rer = ""
    for i in fer:
        rer = rer + i + " "
    return rer[0:-2]
def zaq(dyu1, dyu2):
    but = dict()
    for i in dyu1:
        but[i[0]] = dyu2.count(i[0])
    return but
def tyrh(var1, var2):
    enri = []
    for i in var1:
        for u in var2:
            enri += [[i], [u]],       
    return enri
def hy(doc, sir):
    for i in sir:
        doc = re.sub(fr'\s{i}\s', ' ', doc)
    return doc    
def hu(i):
    stemmer = WordNetLemmatizer()

    # Remove all the special characters
    document = re.sub(r'\W', ' ', i)

    # remove all single characters
    document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)

    document = re.sub(r'\s+[а-яА-Я]\s+', ' ', document)

    document = re.sub(r'\sздравствуйте\s', ' ', document)

    document = hy(document, ["из", "вы", "на", "как", "не", "мы", "это", "от", "за", "наши", "их", "карты", "то", "тинькофф", "tinkoff", "спасибо", "меня", "банк", "банком", "до", "банка"])

    # Remove single characters from the start
    document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)

    # Substituting multiple spaces with single space
    document = re.sub(r'\s+', ' ', document, flags=re.I)

    # Removing prefixed 'b'
    document = re.sub(r'^b\s+', '', document)

    # Converting to Lowercase
    document = document.lower()

    # Lemmatization
    document = document.split()

    document = [stemmer.lemmatize(word) for word in document]
    document = ' '.join(document)
    return document
file = open("save99_utf-8.txt", "r", encoding="utf-8")
text = file.read()
text = text.split('*')[0:500]
#913
#file1 = open("save999_utf-8.txt", "r", encoding="utf-8")
#text1 = file1.read()
#text1 = unite1(text1.split('*')).replace("...Читать далее", " ").split("*")
#text += text1

#729
#print(len(text))#1642
lst00 = []
lst = []
for i in range(len(text)):
    d = TextBlob(hu(text[i]))
    f = hu(text[i]).split(" ")
    polar, subjv = d.sentiment
    if (subjv <= 0.9):
        if (subjv <= 0.9):
            lst00 += ['0']
            lst += ['0']
        if polar>0:
            lst00[-1] = [d, "pos"]
            lst[-1] = [f, "pos"]
        elif polar == 0:
            lst00[-1] = [d, "nor"]
            lst[-1] = [f, "nor"]
        else:
            lst00[-1] = [d, "neg"]
            lst[-1] = [f, "neg"]
        if subjv > 0.8:
            lst00[-1] = lst00[-1] + ["sub"]
            lst[-1] = lst[-1] + ["sub"]
        else:
            lst00[-1] = lst00[-1] + ["nosub"]
            lst[-1] = lst[-1] + ["nosub"]
#print(lst00)
lst1 = []
lst2 = []
lst3 = []
for i in lst:
    if i[1] == "pos":
        lst1 += i
    if i[1] == "nor":
        lst2 += i
    else:
        lst3 += i
lst001 = []
lst002 = []
lst003 = []
for i in lst00:
    if i[1] == "pos":
        lst001 += i
    if i[1] == "nor":
        lst002 += i
    else:
        lst003 += i

#vectorizer = DictVectorizer(max_features=500, max_df=0.7, stop_words=stopwords.words('russian'))
#X = vectorizer.fit_transform(zaq(lst, hu(str(lst)))).toarray()

rut = []
hig = []
sefar = tyrh(lst3, lst3)
safar = tyrh(lst003, lst003)
for i in range(len(sefar)):
    x1 = sefar[i][0][0]
    x2 = sefar[i][1][0]
    if len(x1)!=0 and len(x2)!=0:
        dqr1 = set(x1)
        dqr2 = set(x2)
        sol = dqr1.intersection(dqr2)
        if len(sol) != 0 and x1 != x2:
            pri = hu(str(sol))
            if len(pri) > 3:
                hig += [pri.split(" "), [x1, x2]]
xix = uni1(hig)
for i in hig:
    for y in i[0]:
        if len(i)!=1:
            xix[y] += [une3(i[1])] 
rut += [xix]
hig = []
sefar = tyrh(lst1, lst1)
safar = tyrh(lst001, lst001)
for i in range(len(sefar)):
    x1 = sefar[i][0][0]
    x2 = sefar[i][1][0]
    if len(x1)!=0 and len(x2)!=0:
        dqr1 = set(x1)
        dqr2 = set(x2)
        sol = dqr1.intersection(dqr2)
        if len(sol) != 0 and x1 != x2:
            pri = hu(str(sol))
            if len(pri) > 3:
                hig += [pri.split(" "), [x1, x2]]
xix = uni1(hig)
for i in hig:
    for y in i[0]:
        if len(i)!=1:
            xix[y] += [une3(i[1])]
rut += [xix]
"""
hig = []
sefar = tyrh(lst2, lst3)
safar = tyrh(lst002, lst003)
for i in range(len(sefar)):
    x1 = sefar[i][0][0]
    x2 = sefar[i][1][0]
    if len(x1)!=0 and len(x2)!=0:
        dqr1 = set(x1)
        dqr2 = set(x2)
        sol = dqr1.intersection(dqr2)
        if len(sol) != 0:
            pri = hu(str(sol))
            if len(pri) > 3:
                hig += [pri.split(" "), [x1, x2]]
xix = uni1(hig)
for i in hig:
    for y in i[0]:
        if len(i)!=1:
            xix[y] = xix[y] + [une3(i[1])]
rut += [xix]
"""
file_007 = open('file_700007', "w", encoding="utf-8")
o = f"negative\n"
for a, b in enumerate(rut[0]):
    o += b + " " + unite(rut[0][b]) + f"\n"
o += f"positive\n"
for a, b in enumerate(rut[1]):
    o += b + " " + unite(rut[1][b]) + f"\n"
file_007.write(o)




