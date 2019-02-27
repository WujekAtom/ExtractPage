from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
# name = input("Please provide URL: ")
html = urlopen("https://www.fis-ski.com/DB/general/results.html?sectorcode=JP&raceid=5254")
# html = urlopen(name)
page = BS(html, 'html.parser')
#titles = page.find('div', {'id': 'events-info-results'}).find('div', {'class': 'g-row'})
titles = page.find('div', {'id': 'events-info-results'})
# print(titles)
scores = titles.findAll('div', {'class': 'justify-sb'})
# print(scores)
# print(list(scores.stripped_strings))
# with open("Wyniki.txt", 'w') as f:
with open("Wyniki.txt", 'w') as f:
	for score in scores:
 		# print(score.text)
 		f.write(str(score.text))	
 	# To działa bez stripped_strings
	# time = titles.findAll('div', {'class': 'g-row'})
	# # print(time)
	# print(list(time.stripped_strings))

