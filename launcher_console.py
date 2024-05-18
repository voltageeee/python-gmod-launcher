from webbrowser import open_new
from time import sleep

serverip = '23.88.73.88:13294'

while True:
    serverchoose = input('''
    Please, choose a server with its number.
    Test server- number 1
    Exit - number 0
    TBD...
    ''')

    if not serverchoose.isnumeric():
        print('Please, choose a server number.')
        sleep(3)
    elif serverchoose == '1':
        open_new('steam://connect/'+serverip)
        print('Have a nice time on our server!')
        break
    elif serverchoose == '0':
        print('Bye!')
        sleep(3)
        break