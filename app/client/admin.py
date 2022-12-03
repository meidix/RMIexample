from .stub import ConferenceManager
from datetime import datetime


def show_all_conferences():
    pass

def dispatch_command(command, obj):
    if command == 1:
        print()
        return obj.all()
    elif command == 2:
        info = str(input("Enter the Conference Name: "))
        tickets = str(input('enter the total ticket count: '))
        date_string = str(input("enter conference date[d-MM-YYY]: "))
        date = datetime.strptime(date_string, '%m-%d-%Y').date()
        print()
        return obj.register(conference_info=info, total_tickets=tickets, conference_date=date)
    elif command == 3:
        show_all_conferences()
        index = int(input("enter the number of conference: "))
        name = str(input("enter the participant's name: "))
        age = int(input("enter the participant's age: "))
        print()
        return obj.buy_ticket(index=index, name=name, age=age)
    elif command == 4:
        print()
        return obj.latest()
    elif command == 5:
        print()
        return obj.closest()
    elif command == 6:
        print()
        return 'exit'
    else:
        raise IndexError("Command not available")


def run():
    manager = ConferenceManager()
    print("*** Welcome to Conference Booking Admin App ***")
    while True:
        print('''
        1. Get a list of all the available Conferences
        2. Add a conference
        3. Buy a ticket for a conference
        4. Get the newst conference detail
        5. Get the closest conference today
        6. exit
        ''')
        command = int(input("What do you wish to do?\nenter the number of the operation here:"))
        try:
            result = dispatch_command(command, manager)
            if result == 'exit':
                break
            print('result: ' + str(result))
        except IndexError:
            print(f"command with index {command} does not exist. Please enter a valid Command")
