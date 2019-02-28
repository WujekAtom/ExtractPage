import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen("https://www.fis-ski.com/DB/general/results.html?sectorcode=JP&raceid=5254")
page = BeautifulSoup(html, 'lxml')
page.prettify()

table = page.find_all('a', class_='table-row')  # wyszukuje wiersze z tabeli

trRow = []  # lista kolumn/divów z każdego wiersza
oneJumperResults = [] # tymczasowa lista z wynikami dla jednego, bieżącego skoczka
allJumpersList = [] # lista zawierająca listy ze skoczkami

# iteruje po każdym wierszu i dodaje kolumny [divy] do listy trRow
for tr in table:
    trRow.append(tr.find_all('div'))


# Iteruje po elementach w trRow - trRow zawiera divy z każdego wiersza, czyli jeden element w trRow == wszystkie
# kolumny/divy z jednego wiersza. Trzeba teraz poiterować po tych divach i wyciągnąć z nich informacje

for tc in trRow:
    for i in range(len(tc)):
        if tc[i].string is not None:    # sprawdzam czy DIV nie jest pusty
            tmp = tc[i].string          # wyciągam wartość z DIVa
            oneJumperResults.append(tmp.strip())  # usuwam białe znaki z lewej i prawej i wrzucam do listy
    # dodajemy liste z wynikami kazdego skoczka jako subliste do listy z wszystkimi wynikami
    # allUsersList = [[oneUserResults],[oneUserResults],...]
    allJumpersList.append(oneJumperResults)

    oneJumperResults = [] # czyszcze liste


for j in allJumpersList:
    print(j)
    print('===========================================')
