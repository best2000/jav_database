import re

class star:
    def __init__(self, num, latre, name, mark):
        self.num = num
        self.name = name
        self.latre = latre
        self.mark = mark
    def show(self):
        print(self.num, self.latre, self.name, self.mark)

class config:
    def __init__(self, target_folder_path, filter_folder):
        self.target_folder_path = target_folder_path
        self.filter_folder = filter_folder
    def show(self):
        print(self.target_folder_path, self.filter_folder)

def get_config():
    with open('Settings/config.txt') as f:
        linelis = f.readlines()
    conf_set = [] 
    for line in linelis:
        line = re.split('=', line)
        conf_set.append(line[1][:-1])
    return config(conf_set[0], conf_set[1])

def rewrite_config(config):
    with open('Settings/config.txt', 'w') as f:
        f.write('target_folder_path='+config.target_folder_path+'\nfilter_folder='+config.filter_folder+'\n')

def get_starlis():
    with open("Settings/star_map.txt", 'r') as f:
        linelis = f.readlines()
    #linelis = ['00=dummy\n', '01=aoi tsukasa\n', '02=yui hatano\n', ...]

    starlis = []
    for line in linelis:
        line = re.split('=', line)
        object = star(line[0], line[1], line[2], line[3][:-1])
        starlis.append(object)
    return starlis

def rewrite_star_map(starlis):
    with open('Settings/star_map.txt', 'w') as f:
        for object in starlis:
            f.write(object.num+'='+object.latre+'='+object.name+'='+object.mark+'='+object.javlib+'\n')

def addmark(name):
    starlis = get_starlis()
    for i in range(len(starlis)):
        if starlis[i].name == name:
            starlis[i].mark = "*MUST CHECK*"
            break
    rewrite_star_map(starlis)

def clrmark():
    starlis = get_starlis()
    for i in range(len(starlis)):
        if starlis[i].mark == "*RETIRED*":
            continue
        starlis[i].mark = ""
    rewrite_star_map(starlis)

def newlatre(date, name):
    starlis = get_starlis()
    for i in range(len(starlis)):
        if starlis[i].name == name:
            starlis[i].latre = date
            break
    rewrite_star_map(starlis)

