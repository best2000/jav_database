import requests, re, subprocess, random
from bs4 import BeautifulSoup
from class_register import *

def javmost_check_latest():
    starlis = get_starlis()
    for object in starlis:
        name = re.split(' ', object.name)
        n1 = name[0]
        n2 = name[1]
        n1 = n1[0].upper()+n1[1:]
        n2 = n2[0].upper()+n2[1:]
        url = 'https://www5.javmost.com/star/'+n1+'%20'+n2+'/'
        r = requests.get(url)
        print(r)
        print(url)
        try:
            page = BeautifulSoup(r.text, 'html.parser')
            lascard = page.find(class_='card-text')
            date = lascard.contents[2]
            date = re.split('-', date)
            date = [date[0][9:],date[1],date[2][0]+date[2][1]]
            dbformat = date[0]+'-'+date[1]+'-'+date[2]
            print("Latest:", dbformat)
            print("Old:", object.latre)
            olddate = re.split('-', object.latre)
            if olddate[0] < date[0]:
                addmark(object.name)
                newlatre(dbformat, object.name)
            elif olddate[0] == date[0]:
                if olddate[1] < date[1]:
                    addmark(object.name)
                    newlatre(dbformat, object.name)
                elif olddate[1] == date[1]:
                    if olddate[2] < date[2]:
                        addmark(object.name)
                        newlatre(dbformat, object.name)
                        
        except:
            print('NOT FOUND!')
        

