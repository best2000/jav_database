import os, fnmatch, shutil, random, subprocess
from class_register import *

def filtered_clr():
    c = get_config()
    fil_file = os.listdir(c.target_folder_path+c.filter_folder)
    if len(fil_file) != 0:
        for fname in fil_file:
            shutil.move(c.target_folder_path+c.filter_folder+fname, c.target_folder_path+fname)

def star_match_file(name):
    filtered_clr()
    name = name.lower()
    starlis = get_starlis()
    for object in starlis:
        if object.name == name or object.num == name:
            match_star = object
            break
    if match_star == None:
        print("star not found!")
        return
    c = get_config()
    os.rename(c.target_folder_path+c.filter_folder, c.target_folder_path+match_star.name)
    c.filter_folder = match_star.name+'/'
    rewrite_config(c)
    match_file = []
    for f_name in os.listdir(c.target_folder_path):
        if fnmatch.fnmatch(f_name, '*#'+match_star.num+'*'):
            match_file.append(f_name)

    for i in match_file:
        shutil.move(c.target_folder_path+i, c.target_folder_path+c.filter_folder+i)
    subprocess.run(['start', 're.bat'], shell=True)
    #statadd(name)
    
            
def rand_star():
    starlis = get_starlis()
    rand = random.randint(0,len(starlis)-1)
    filtered_clr()
    star_match_file(starlis[rand].name)
    print("result :", starlis[rand].name)

def showall():
    starlis = get_starlis()
    for object in starlis:
        object.show()

def showre():
    starlis = get_starlis()
    for object in starlis:
        print(object.latre, object.name, object.mark)


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
                print(object.name)
                
