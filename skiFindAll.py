from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
html = urlopen("https://www.fis-ski.com/DB/general/results.html?sectorcode=JP&raceid=5322")

page = BS(html.read(), 'html.parser')

# titles = page.find('div', {'id': 'events-info-results'}).findAll('div', {'class': 'justify-sb'})
# print(len(titles));

tableRow = page.findAll("a", {'class':"table-row"})
trRow =[]

for rows in tableRow:
    trRow.append(rows.findAll('div', {'class':['justify-right', 'justify-left']}));
    # rows.findAll('div', {'class': ['justify-right', 'justify-left']})[0].decode_contents()
# trRow[0].decode_coon
for i in trRow:
    for n in range(0,len(trRow)):
        j = i[n].decode_contents();
        print(j)
    # for j in i:
    #     for k in j:
    #       print(k)
#
# with open("WorldCup.txt", "w") as f:
# for td in titles:
#     score = td.select("div").get_text()
#     print(score)
#         f.write(str(td));
#     for table in titles:
#         container = table.findAll('div')
#     print(container)