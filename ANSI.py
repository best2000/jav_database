import os

def reset():
    print("\u001b[0m")

class colors:
    
    def __init__(self):
        self.re = "\u001b[0m"

        self.black = "\u001b[30m"
        self.red = "\u001b[31m"
        self.green = "\u001b[32m"
        self.yellow = "\u001b[33m"
        self.blue = "\u001b[34m"
        self.magenta = "\u001b[35m"
        self.cyan = "\u001b[36m"
        self.white = "\u001b[37m"
        
        self.black_bg = "\u001b[40m"
        self.red_bg = "\u001b[41m"
        self.green_bg = "\u001b[42m"
        self.yellow_bg = "\u001b[43m"
        self.blue_bg = "\u001b[44m"
        self.magenta_bg = "\u001b[45m"
        self.cyan_bg = "\u001b[46m"
        self.white_bg = "\u001b[47m"

        self.bold = "\u001b[1m"
        self.underline = "\u001b[4m"
        self.reverse = "\u001b[7m"

        

    def reset(self):
        print(self.re)

    def on(self, **kwargs):
        try: 
            if kwargs['target'] == 'text': 
                print(self.green) 
            elif kwargs['target'] == 'background':
                print(self.green) 
            if kwargs['']
        except: pass

os.system('cls')
c = colors()
c.green(state='on')

print('lol')
c.reset()