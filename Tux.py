__author__ = 'OliPicard'
import re
import sys


'''
Tux the friendly AI
Developed by OliPicard - github.com/olipicard/tux/
This program is licenced under the GPL GNU 3.0 licence.
'''


def menu():
    tux = '''
        .--.
       |o_o |
       |:_/ |
      //   \ \|
     (|     | )
    /'\_   _/`\|
    \___)=(___/
    '''
    print(tux)
    print('Welcome to Tux, Your friendly, intelligent AI.')
    print('This program is licenced under the GPL GNU 3.0 licence.')



def lmgtfy():
    words = input('Ok, So how can I be of assistance? ')
    if words == 'quit' or 'exit':
        sys.exit()
    elif words == 'credits':
        print('Tux was created by OliPicard. full source code at github.com/olipicard/tux')
        print('This program is licenced under the GPL GNU 3.0 licence.')
        print('Original idea from /r/linux/')
        print('Tux is the official mascot of Linux.')
    elif words == 'help':
        print('Simply ask me any question. to quit the application type quit.')
    else:
        url = 'http://lmgtfy.com/?q='
        output = re.sub('\s', '+', words.rstrip())
        print('Ok, Here\'s what i\'ve found\n'+url + output)
        input('Press any key to return back to the main menu.')

loopy = True

while loopy:
    menu()
    lmgtfy()