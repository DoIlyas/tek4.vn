logged_in = False

while logged_in == False:
    loggin_username = input('Username: ')
    if loggin_username != 'duong':
        print('Username is invalid!')
    else:
        loggin_password = input('Password: ')
        if loggin_password == 'asdpoi':
            print('Loggin Success!')
            logged_in = True
        else:
            print('Password is incorrect!')