# toolkit for programming

# libaries
import datetime

class log:

    def message(text):
        print(f'> [PROGRAM {datetime.datetime.now()}]: {str(text)}')

    def error(text):
        print(f'> [ERROR {datetime.datetime.now()}]: {str(text)}')
