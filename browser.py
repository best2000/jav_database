import os, fnmatch, shutil, random
from class_register import *

def statadd(name):
    starlis = get_starlis()
    for i in range(len(starlis)):
        if starlis[i].name == name:
            starlis[i].stat = str(int(starlis[i].stat)+1)
            print('stat :', starlis[i].name, '+1')
            break

    with open('Settings/star_map.txt', 'w') as f:
        for object in starlis:
            f.write(object.num+'='+object.name+'='+object.stat+'\n')
        f.write("EOF")

def filtered_clr():
    with open("Settings/filfol.txt", 'r') as f:
        di = f.read()
    fil_file = os.listdir('Empire of the Rising Sun/'+di)
    if len(fil_file) != 0:
        for fname in fil_file:
            shutil.move('Empire of the Rising Sun/'+di+'/'+fname, 'Empire of the Rising Sun/'+fname)

def star_match_file(name): #return filename lis
    filtered_clr()
    name = name.lower()
    starlis = get_starlis()
    for object in starlis:
        if object.name == name or object.num == name:
            match_star = object
            break
    if match_star == None:
        print("star not found!")
    with open("Settings/filfol.txt", 'r') as f:
        di = f.read()
    os.rename('Empire of The Rising Sun/'+di, 'Empire of The Rising Sun/star='+match_star.name)
    with open("Settings/filfol.txt", 'w') as f:
        f.write('star='+match_star.name)
    di = 'star='+name
    match_file = []
    for f_name in os.listdir('Empire of the Rising Sun'):
        if fnmatch.fnmatch(f_name, '*#'+match_star.num+'*'):
            match_file.append(f_name)

    for i in match_file:
        shutil.move('Empire of the Rising Sun/'+i, 'Empire of the Rising Sun/'+di+'/'+i)
    statadd(name)
    
            
def rand_star():
    starlis = get_starlis()
    rand = random.randint(0,len(starlis)-1)
    filtered_clr()
    star_match_file(starlis[rand].name)
    print("result :", starlis[rand].name)

def showall():
    starlis = get_starlis()
    for object in starlis:
        print(object.num, object.name, object.stat)

def show_sort_stat():
    starlis = get_starlis()
    statlis = []
    for object in starlis:
        statlis.append(int(object.stat))
    statlis.sort()
    for stat in statlis:
        for object in starlis:
            if object.stat == str(stat):
                starlis.remove(object)
                print(object.stat, object.name)

def show_sort_name():
    starlis = get_starlis()
    namelis = []
    for object in starlis:
        namelis.append(object.name)
    namelis.sort()
    for name in namelis:
        for object in starlis:
            if object.name == name:
                starlis.remove(object)
                print(object.name, object.stat)
                