from .stub import ConferenceManager

def show_all_conferences():
    print('Conferences')

def run():
    manager = ConferenceManager.manager()
    print("***Welcome To The Conference Booking App***")
    print("Here is a list of all the available Conferences right now.")
    while True:
        show_all_conferences()
        conference_index = int(input("To buy a ticket for a conference, plase enter the number of the conference here: "))
        name = str(input("Please enter the name of the person you're buying ticket for: "))
        age = str(input('How old is this person: '))
        manager.buy_ticket(conference_index, name, age)
        print(f'1 ticket for {name} was reserved. thanks for your purchase')
        exit_flag = str(input('Do you like to continue? [y/n] '))
        if exit_flag == 'n':
            break
