import re

class star:
    def __init__(self, num, latre, name, stat, mark):
        self.num = num
        self.name = name
        self.stat = stat
        self.latre = latre
        self.mark = mark
    def show(self):
        print(self.num, self.latre, self.name, self.stat, self.mark)

def get_starlis():
    linelis = []
    with open("Settings/star_map.txt", 'r') as file:
        while True:
            line = file.readline()
            if line == "EOF":
                break
            linelis.append(line)
    #linelis = ['00=dummy\n', '01=aoi tsukasa\n', '02=yui hatano\n', ...]

    starlis = []
    for line in linelis:
        line = re.split('=', line)
        object = star(line[0], line[1], line[2], line[3], line[4][:-1])
        starlis.append(object)
    return starlis

def rewrite_star_map(starlis):
    with open('Settings/star_map.txt', 'w') as f:
        for object in starlis:
            f.write(object.num+'='+object.latre+'='+object.name+'='+object.stat+'='+object.mark+'\n')
        f.write("EOF")

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