import random 
from pyfiglet import Figlet
from termcolor import colored

fonts = [ 'slant', 'banner3-D', 'big', 'block', 
         'bubble', 'digital', 'doom', 'isometricl',
         'mini', 'small', 'starwars']
colors = ['red', 'green', 'yellow', 'bleu',
          'magenta', 'cyan']

F = Figlet(font=random.choice(fonts))
print(colored(F.renderText(" waldja monyabte cyrille "), random.choice(colors)))
#source code --> 