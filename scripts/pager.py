import requests
from bs4 import BeautifulSoup
import os

import html_code

dir_path = os.path.dirname(os.path.realpath(__file__))

# base = "https://www."

langs = {
    "english":'woerter.net',"deutsch":'verben.de',"русский":'woerter.ru'
}
# with open("de.txt",'r') as file:
#     data = file.readlines()
    
# word = data[5].split(" ")[0].replace("!","")

def page(lang,word):
    url = langs[lang.lower()]
    
    r= requests.get(f"https://www.{url}/?w={word.lower()}")
    
    soup = BeautifulSoup(r.text, 'html.parser')
    
    #title
    title = soup.find("p",{"class":"rCntr rClear"})
    title = title.findChildren("span")
    title = '\n:'.join(str(item) for item in title)

    #Synonyms and meaning
    meaning_and_synonyms = soup.findAll("div",{"class":"rAufZu"})
    li=[]
    
    for i in meaning_and_synonyms[:4]:
        x = i.findChildren("dl")
        x = '\n'.join(str(item) for item in x)
        if x != "":
            li.append(x)
            
    example= soup.find("ul",{"class":"rLst"})

    # if len(li)<2:
    #     html_code.synonym1 = ''
    #     html_code.closing2 = ''
    #     li.append('')
        
    html = html_code.make(lang, title, li, example, r.url).replace("<a href=\"",f"<a href=\"https://www.{url}")
    file_path = f"{dir_path}/../htmls/{word}_{lang.lower()}.html"
    try:
        with open(file_path,'w',encoding='UTF-8') as file:
            file.write(html)
        
        main_word = title.split("q>")[1][:-2]
        article = title.split("</span>")[1][-3:]
        pretty_word = f"{article} {main_word}".capitalize()
    except:
        pass
    
    return pretty_word,file_path,r.url


# print("Русский".lower())