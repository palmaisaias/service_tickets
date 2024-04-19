import colorama     #give it a little umphh
from colorama import Back, Fore, Style
colorama.init
colorama.init(autoreset=True)

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def new_tix():
    while True:
        new_tic = input('Assign a new ticket number: ')
        new_name = input("What is the customer's name? ")
        new_issue = input('What is the issue? ')
        new_status = 'open' #sets default status to 'open'
        print(Fore.GREEN + f'               Thank you for opening ticket: {new_tic}\n')
        service_tickets[new_tic] = {"Customer": new_name, "Issue": new_issue, "Status": new_status}
        return service_tickets
    
def update_status():
    while True:
        while True: #Didnt necessarily want to nest a while loop but it really like the option of giveing the user the opportunity to view the list
            convenience = input('Would you like to see a list of your current service ticket numbers?(y/n) ')
            if convenience == 'y':
                for i in service_tickets:
                    print(i)    #prints nicely
                print()
                break   #SUPER important to break. 
            elif convenience == 'n':
                break   #note to break the loop!
            else:
                print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "            Please enter either 'y' or 'n'")
        try:
            update = input('Which ticket would you like to update status on? ')
            print()
            if update not in service_tickets:
                raise KeyError(f'{update} is not a current ticket') #raises the key error
            stat = input("Enter status as 'open' , 'closed' or any custom message? ") #custom message option convenient AND avoids another while loop
            service_tickets[update]['Status'] = stat
            print(Fore.GREEN + f'               You have updated: {update} to {stat.upper()}\n') #uppercase status prints nicely
            break
        except KeyError as grace:
            print(Fore.RED + Style.BRIGHT + str(grace) + Fore.RESET, '\n')  #was stuck here. without noting 'grace' as a 'str', Colorama prints gibberish instead of actioning the color and style
            print(Fore.LIGHTRED_EX + '                      Please, try again\n')
    return service_tickets  #make sure NOT in the while loop otherwise it kicks to MENU after any incorrect ticket number attempt

def display_tix():
    for tic, inf in service_tickets.items():    #saw this on W3 schools and it outputs dictionaries beautifuly. 'tic' being the key and 'inf' being the value.
        print() #this little space is clutch. This was NOT on W3 schools haha
        print(tic)
        for key in inf:    #nested 'for loop' outputs nested dictionaries nicely
            print(key +':', inf[key])   #adding the colon gives more 'readable' list

def manage_tickets():
    while True:
        print()
        print('''                  Welcome to Ticket Manager
              -----------------------------------
              1. Open a new service ticket
              2. Update status on existing ticket
              3. Display all tickets
              4. Quit\n''')
        choice = input(Style.BRIGHT + '                Enter menu option 1,2,3, or 4: ' + Style.RESET_ALL)
        print()
        if choice == '1':
            new_tix()
        elif choice == '2':
            update_status()
        elif choice == '3':
            display_tix()
        elif choice =='4':
            print(Style.BRIGHT + Fore.LIGHTBLUE_EX + '              Thank you for using Ticket Manager!\n')
            break
        else:
            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT +'       Please enter the NUMBER of the menu option you need')


manage_tickets()