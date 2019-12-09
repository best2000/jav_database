import re, subprocess
from browser import *

help = """
COMMANDS 
showall                         show all star info
showsort=<stat/name>        show sorted attrbute
star=<name/num>                 filter this star only
random                          random star
star_map.txt                    open database text file
"""

while True:
    cmd = re.split('=', input('cmd : '))
    if cmd[0] == 'showall': showall()
    elif cmd[0] == 'showsort': 
        try:
            if cmd[1] == "stat": show_sort_stat()
            elif cmd[1] == "name" : show_sort_name()
        except Exception as e: print(e)
    elif cmd[0] == 'star':
        try: star_match_file(cmd[1])
        except Exception as e: print(e)
    elif cmd[0] == 'star_map.txt': subprocess.run(['start', 'star_map.txt'], shell=True) #for windows
    elif cmd[0] == 'random': rand_star()
    elif cmd[0] == "exit": break
    elif cmd[0] == "help": print(help)