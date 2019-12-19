import re, subprocess, os
from browser import *
from scrapy import *
os.system('cls')

#suggest star name system

help = """
COMMANDS 
showall                         show all star info
showsort=<name>                 show sorted attrbute
star=<name/num>                 filter this star only
random                          random star
latrecheck=<online/offline>     new release check if online => check from javmost and auto mark and update star_map.txt
                                                     offline=> check from star_map.txt file
clrmark                         clear all marks
star_map.txt                    open database text file
"""
print("\u001b[31;1m")
print('jav_filter\n')

while True:
    cmd = re.split('=', input('cmd : '))
    if cmd[0] == 'showall': show_sort_name()
    elif cmd[0] == 'showsort': 
        try:
            if cmd[1] == "name" : pass
        except Exception as e: print(e)
    elif cmd[0] == 'star':
        try: star_match_file(cmd[1])
        except Exception as e: print(e)
    elif cmd[0] == 'latrecheck': 
        try: 
            if cmd[1] == 'online': javmost_check_latest()
            elif cmd[1] == 'offline': showre()
        except Exception as e: print(e)
    elif cmd[0] == 'star_map.txt': subprocess.run(['start', 'star_map.txt'], shell=True) #for windows
    elif cmd[0] == 'random': rand_star()
    elif cmd[0] == 'clrmark': clrmark()
    elif cmd[0] == "exit": 
        print('\u001b[0m')
        break
    elif cmd[0] == "help": print(help)