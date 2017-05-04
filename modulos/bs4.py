import bs4 as bs
import lxml
import requests


def busca(string):
    texto_html = requests.GET('https://www.google.com.br'+string)

    bs_obj = bs.BeautifulSoup(texto_html.text(), 'lxml') # continua em html porém como objeto bs4

    #bs_obj.title.string titulo 
    # bs_obj.find_all('p') ## google -> div data-hveid

    for paragraph in soup.find_all('p'): # texto na tag
        print(paragraph.text)

    for url in bs_obj.find_all('a'): # links
        print(url.get('href'))

    for div in soup.find_all('div', class_='g'):
        print(div.text)

        
# YOUTUBE        
#class_="yt-lockup-content"
#<a.title>
# a.data-ytid

#receber sites como entrada, ex
# olx -> procura todos os produtos escolhidos
# mercado livre 
# facebook
# yt
# google
# steam
# github
# https://www.youtube.com/watch?v=3xQTJi2tqgk
