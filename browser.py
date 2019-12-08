import os, fnmatch, subprocess
from class_register import *

def star_match_file(name): #return filename lis
    name = name.lower()
    starlis = get_starlis()
    for object in starlis:
        if object.name == name or object.num == name:
            match_star = object
    match_file = []
    for f_name in os.listdir('test_data'):
        if fnmatch.fnmatch(f_name, '*#'+match_star.num+'*'):
            match_file.append(f_name)
    
    return match_file

def match_file_name(name): #return filename lis
    match_file = []
    for f_name in os.listdir('test_data'):
        if fnmatch.fnmatch(f_name, '*'+name+'*'):
             match_file.append(f_name)
    
    return match_file

def open_vid(fpath):
    subprocess.run(['start', fpath], shell=True) #for windows

print(match_file_name("ssni"))