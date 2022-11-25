import ip_checker

menu_options = {
    1: 'Check host for connected malicious IPs',
    2: 'Option 2',
    3: 'Option 3',
    4: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
    print('============================')
    ip_checker.bad_stuff()
    print('============================') 

def option2():
     pass

def option3():
     pass

if __name__ == '__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            print('Quitting....')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')