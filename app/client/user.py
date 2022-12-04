from .stub import ConferenceManager

def show_all_conferences(manager):
    conferences = manager.all()
    if len(conferences) == 0:
        print("There are no available conferences")
        return
    count = 1
    for conf in conferences:
        print(f'{count}.\t\t{conf.conference_info}\t{conf.conference_date}\t{conf.remaining_tickets}')
        count += 1

def run():
    manager = ConferenceManager()
    print("***Welcome To The Conference Booking App***")
    print("Here is a list of all the available Conferences right now.")
    while True:
        show_all_conferences(manager)
        conference_index = int(input("To buy a ticket for a conference, plase enter the number of the conference here: "))
        name = str(input("Please enter the name of the person you're buying ticket for: "))
        age = int(input('How old is this person: '))
        manager.buy_ticket(conference_index - 1, name, age)
        print(f'1 ticket for {name} was reserved. thanks for your purchase')
        exit_flag = str(input('Do you like to continue? [y/n] '))
        if exit_flag == 'n':
            break
