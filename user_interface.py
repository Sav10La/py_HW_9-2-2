import control as cl
import logger as lg


print('\nWelcome to the phone book!')


def ls_menu():
    while True:
        print('\nMenu:')
        print('1. Show all entries.')
        print('2. Find phone number by last name.')
        print('3. Find phone number by name.')
        print('4. Search by phone number.')
        print('5. Add new entry.')
        print('6. Edit an existing entry.')
        print('7. Delete an entry.')
        print('8. Close program.\n')
        n = сhecking_the_number(input('Choose menu item: '))

        if n == 1:
            lg.logging.info('The user has selected item number 1')
            print('1. Display entry as a row.')
            print('2. Display entry as a paragraph.' '\n')
            display = сhecking_the_number(input('Enter item number: '))
            if display == 1:
                lg.logging.info('The user has selected item number 1.1')
            elif display == 2:
                lg.logging.info('The user has selected item number 1.2')
            print(cl.retrieve(format=display))


        elif n == 2:
            lg.logging.info('The user has selected item number 2')
            search = input('Enter last name: ')
            lg.logging.info('User entered: {search}')
            print(cl.retrieve(last_name=search))

        elif n == 3:
            lg.logging.info('The user has selected item number 3')
            search = input('Enter name: ')
            lg.logging.info('User entered: {search}')
            print(cl.retrieve(name=search))

        elif n == 4:
            lg.logging.info('The user has selected item number 4')
            search = input('Enter phone number: ')
            lg.logging.info('User entered: {search}')
            print(cl.retrieve(number=search))

        elif n == 5:
            lg.logging.info('The user has selected item number 5')
            name = input('Enter name: ')
            lg.logging.info('User entered: {name}')
            last_name = input('Enter last name: ')
            lg.logging.info('User entered: {last_name}')
            number = input('Enter phone number: ')
            lg.logging.info('User entered: {number}')
            email = input('Enter email: ')
            lg.logging.info('User entered: {email}')
            cl.create(name, last_name, number, email)

        elif n == 6:
            lg.logging.info('The user has selected item number 6')
            print('1. Find phone number by last name.')
            print('2. Find phone number by name.')
            print('3. Search by phone number.')
            edit = сhecking_the_number(input('Enter item number: '))

            if edit == 1:
                lg.logging.info('The user has selected item number 6.1')
                search = input('Enter last name: ')
                lg.logging.info('User entered: {search}')
                cl.retrieve(last_name=search)
                user_id = input('Enter entry id: ')
                lg.logging.info('User entered: {user_id}')
                new_number = input('Enter new phone number: ')
                lg.logging.info('User entered: {new_number}')
                cl.update(id=user_id, new_number=new_number)

            elif edit == 2:
                lg.logging.info('The user has selected item number 6.2')
                search = input('Enter name: ')
                lg.logging.info('User entered: {search}')
                cl.retrieve(name=search)
                user_id = input('Enter entry id: ')
                lg.logging.info('User entered: {user_id}')
                new_number = input('Enter new phone number: ')
                lg.logging.info('User entered: {new_number}')
                cl.update(id=user_id, new_number=new_number)

            elif edit == 3:
                lg.logging.info('The user has selected item number 6.3')
                search = input('Enter phone number: ')
                lg.logging.info('User entered: {search}')
                cl.retrieve(number=search)
                user_id = input('Enter entry id: ')
                lg.logging.info('User entered: {user_id}')
                new_number = input('Enter new phone number: ')
                lg.logging.info('User entered: {new_number}')
                cl.update(id=user_id, new_number=new_number)

            else:
                lg.logging.info('User entered an invalid menu value')
                print(
                    '\nSuch menu item does not exist.\nEnter the number corresponding to the menu item.')

        elif n == 7:
            lg.logging.info('The user has selected item number 7')
            print('1. Find phone number by last name.')
            print('2. Find phone number by name.')
            print('3. Search by phone number.')
            deleting = сhecking_the_number(input('Enter item number: '))

            if deleting == 1:
                lg.logging.info('The user has selected item number 7.1')
                search = input('Enter last name: ')
                lg.logging.info('User entered: {search}')
                print(cl.retrieve(last_name=search))
                user_id = input('Enter entry id: ')
                lg.logging.info('User entered: {user_id}')
                cl.delete(id=user_id)

            elif deleting == 2:
                lg.logging.info('The user has selected item number 7.2')
                search = input('Enter name: ')
                lg.logging.info('User entered: {search}')
                print(cl.retrieve(name=search))
                user_id = input('Enter entry id: ')
                lg.logging.info('User entered: {user_id}')
                cl.delete(id=user_id)

            elif deleting == 3:
                lg.logging.info('The user has selected item number 7.3')
                search = input('Enter phone number: ')
                lg.logging.info('User entered: {search}')
                print(cl.retrieve(number=search))
                user_id = input('Enter entry id: ')
                lg.logging.info('User entered: {user_id}')
                new_number = input('Enter new phone number: ')
                cl.delete(id=user_id)

            else:
                lg.logging.info('User entered an invalid menu value')
                print(
                    '\nSuch menu item does not exist.\nEnter the number corresponding to the menu item.')

        elif n == 8:
            lg.logging.info('End')
            print('Bye bye!')
            break

        else:
            lg.logging.info('User entered an invalid menu value: {n}')
            print(
                '\nSuch menu item does not exist.\nEnter the number corresponding to the menu item.')

def сhecking_the_number(arg):
    while arg.isdigit() != True:
        lg.logging.info('User entered an invalid menu value: {arg}')
        print('\nYou did not enter number.')
        arg = input('Enter existing menu item: ')
    return int(arg)