import requests
import time
import pandas as pd
import re
from bs4 import BeautifulSoup

noticies_list=[]

#Consultando cuántas páginas tiene
page = requests.get('https://periodicodelmeta.com/category/villavicencio/')
soup = BeautifulSoup(page.content, 'html.parser')
a = soup.find(class_="last")
pages=a.get_text()
pages= re.sub("\.","",pages)

#for pages in range(1,int(pages)+1): #Para todas las páginas
for pages in range(1,5+1):    #Para una cantidad específica de páginas
    #Receta página
    page = requests.get('https://periodicodelmeta.com/category/villavicencio/page/'+str(pages))
    soup = BeautifulSoup(page.content, 'html.parser')
    noticies = soup.find_all(class_='td_module_10')
    
    for x in range(0,2):
        #Scrapeamos elementos
        title = noticies[x].find(class_='entry-title td-module-title')
        title = title.find('a').get('title')
        link_news = noticies[x].find(class_='td-image-wrap')
        link_news = link_news.get('href')
        date = noticies[x].find(class_='entry-date')
        date = date.get('datetime')
        description = noticies[x].find(class_='td-excerpt').text

        #Enviamos a Dataframe
        data = {"title":title,"date":date,"link":link_news}
        noticies_list.append(data)    
    time.sleep(0.5)

dataframe=pd.DataFrame(noticies_list)
print(dataframe)