import pandas as pd
import requests
import re

#simpsons_wiki=requests.request("https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1–20)","r")

website = requests.get("https://es.wikipedia.org/wiki/Anexo:Películas_del_Universo_cinematográfico_de_Marvel")#, auth=('user', 'pass'))
website = website.text
tables = pd.read_html(website, encoding="UTF-8")
start = re
#for i in range(1,6):
pelis = tables[1]
#print(list(pelis))
#print(pelis['Película'],pelis['Estreno en EE.\xa0UU.'])
print(pelis.iloc[0:5, 0:2])