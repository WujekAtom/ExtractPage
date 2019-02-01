from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
name = input("Please provide URL: ")
# html = urlopen("https://www.fis-ski.com/DB/general/results.html?sectorcode=JP&raceid=5254")
html = urlopen(name)
page = BS(html, 'html.parser')
titles = page.find('div', {'id': 'events-info-results'}).find('div', {'class': 'g-row'})
# print(titles)
# print(list(titles.stripped_strings))
with open("Skoki.txt", "w") as f:
    f.write(str(list(titles.stripped_strings)))
#     for td in titles.div:
        # pd = td.stripped_strings
        # f.write(pd)
        # f.write(str(pd))


#  <div class="resultview">
#resultlist