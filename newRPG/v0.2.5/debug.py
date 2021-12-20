import os
from data import *

class debug:

    errType = {
        'e': '[{}ERROR_{}]:'.format(textColor['red_b'], textColor[defaultColor]),
        's': '[{}SYSTEM{}]:'.format(textColor['wht_b'], textColor[defaultColor]),
        'd': '[{}DEBUG_{}]:'.format(textColor['gry_b'], textColor[defaultColor]),
    }
    def log(type, message):
        print(debug.errType[type], str(message))
    
    def clear():
        os.system('CLS')

    def input(inputData):
        userInput = innput(inputData)