#importing modules from python std library

#This way we import all the library
#import random
#import sys
#import os
import math

#We can also import just what we need
#(from random import *) with the * we import all the library
#we can substitute the * whit the function that we need

from random import randint

#sometimes we want to exit the program early
#to do that we can use the sys.exit() function

import sys
#sys.exit()

#we can also import third party libraries by first installing them with pip
#from the CLI
#ex: pip install pyperclip

#Then in the program we can import it
#import pyperclip
#pyperclip.copy("Some text")
#pyperclip.paste()