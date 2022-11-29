import sys
from app.client import user, admin
from app.server import server


def main():
    '''this is the main entery of the whole app. it manages all the needed servers'''
    try:
        file_to_run = str(sys.argv[1])
    except:
        print('''
        one of the following arguments should be provided:
        runserver
        runuser
        runadmin
        No Command Found
        ''')
    if file_to_run == 'runserver':
        server.run()
    elif file_to_run == 'runuser':
        user.run()
    elif file_to_run == 'runadmin':
        admin.run()
    else:
        print('''
        Command Does not Exist!!
        available commands:
        runserver,
        runuser,
        runadmin
        ''')


if __name__ == '__main__':
    main()