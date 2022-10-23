import telebot
import control as cl
import logger as lg


token = '5619401271:AAFZxGjbYQPyzWcqg-J2-9CdknDhbNF7l6I'
bot = telebot.TeleBot(token, parse_mode='MARKDOWN')


@bot.message_handler(content_types=['sticker', 'pinned_message', 'photo', 'audio', 'video'])
def warning(message):
    bot.send_message(
        message.chat.id, f'I do not understand you. Enter: /help.')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, f'Hi, *{message.from_user.first_name}!*\nIn any unclear situation, enter\ncommand: /help\nYep! buttons will appear soon ;)\nTo see the main menu, enter: /main')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(
        message.chat.id, f'/start - start anew (relaunch bot)\n/main - main menu\n/help - call help')


name_it = ''
surname_it = ''
number_it = ''
email_it = ''
user_id_it = ''
new_number_it = ''


@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == '/main':
        bot.send_message(message.chat.id, f'Select a menu item by entering the corresponding command: \n/1 - Show all entries.\n/2 - Find phone number by last name.\n/3 - Find phone number by name.\n/4 - Search by phone number.\n/5 - Add new entry.\n/6 - Edit an existing entry.\n/7 - Delete an entry.')
        cl.init_data_base('base_phone.csv')

    elif message.text == '/1':
        lg.logging.info('The user has selected item number 1')
        bot.send_message(message.chat.id, f'{cl.retrieve()}')

    elif message.text == '/2':
        lg.logging.info('The user has selected item number 2')
        bot.send_message(message.chat.id, f'Enter surname')
        bot.register_next_step_handler(message, find_surname)

    elif message.text == '/3':
        lg.logging.info('The user has selected item number 3')
        bot.send_message(message.chat.id, f'Enter name')
        bot.register_next_step_handler(message, find_name)

    elif message.text == '/4':
        lg.logging.info('The user has selected item number 4')
        bot.send_message(message.chat.id, f'Enter phone number')
        bot.register_next_step_handler(message, find_number)

    elif message.text == '/5':
        lg.logging.info('The user has selected item number 5')
        bot.send_message(message.chat.id, f'Enter name')
        bot.register_next_step_handler(message, get_name)

    elif message.text == '/6':
        lg.logging.info('The user has selected item number 6')
        bot.send_message(
            message.chat.id, f'Which entry do you want to edit?\nSpecify by:\n/61 - Surname\n/62 - Name\n/63 - Phone number')
        bot.register_next_step_handler(message, edit_entry)

    elif message.text == '/7':
        lg.logging.info('The user has selected item number 7')
        bot.send_message(
            message.chat.id, f'Select the contact you want to delete?\nSpecify by:\n/71 - Surname\n/72 - Name\n/73 - Phone number')
        bot.register_next_step_handler(message, delete_contact)

    else:
        bot.send_message(
            message.chat.id, f'I do not understand you. Enter: /help.')


def find_surname(message):
    global surname_it
    surname_it = message.text
    lg.logging.info('User entered: {surname_it}')
    bot.send_message(message.chat.id, f'{cl.retrieve(last_name=surname_it)}')


def find_name(message):
    global name_it
    name_it = message.text
    lg.logging.info('User entered: {name_it}')
    bot.send_message(message.chat.id, f'{cl.retrieve(name=name_it)}')


def find_number(message):
    global number_it
    number_it = message.text
    lg.logging.info('User entered: {number_it}')
    bot.send_message(message.chat.id, f'{cl.retrieve(number=number_it)}')


def get_name(message):
    global name_it
    name_it = message.text
    lg.logging.info('User entered: {name_it}')
    bot.send_message(message.chat.id, f'Enter surname')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname_it
    surname_it = message.text
    lg.logging.info('User entered: {surname_it}')
    bot.send_message(message.chat.id, f'Enter phone number')
    bot.register_next_step_handler(message, get_number)


def get_number(message):
    global number_it
    number_it = message.text
    lg.logging.info('User entered: {number_it}')
    bot.send_message(message.chat.id, f'Enter email')
    bot.register_next_step_handler(message, get_email)


def get_email(message):
    global email_it
    email_it = message.text
    lg.logging.info('User entered: {email_it}')
    cl.create(name_it, surname_it, number_it, email_it)
    bot.send_message(message.chat.id, f'Entry added successfully!')


def edit_entry(message):
    if message.text == '/61':
        lg.logging.info('The user has selected item number 6.1')
        bot.send_message(message.chat.id, f'Enter surname')
        bot.register_next_step_handler(message, change_surname)

    elif message.text == '/62':
        lg.logging.info('The user has selected item number 6.2')
        bot.send_message(message.chat.id, f'Enter name')
        bot.register_next_step_handler(message, change_name)

    elif message.text == '/63':
        lg.logging.info('The user has selected item number 6.3')
        bot.send_message(message.chat.id, f'Enter phone number')
        bot.register_next_step_handler(message, change_num)

    else:
        bot.send_message(
            message.chat.id, f'I do not understand you. Enter: /help.')


def change_name(message):
    global name_it
    name_it = message.text
    lg.logging.info('User entered: {name_it}')
    bot.send_message(message.chat.id, f'{cl.retrieve(name=name_it)}')
    bot.send_message(
        message.chat.id, f'Enter id of entry, which you want to edit')
    bot.register_next_step_handler(message, change_number)


def change_surname(message):
    global surname_it
    surname_it = message.text
    lg.logging.info('User entered: {surname_it}')
    bot.send_message(message.chat.id, f'{cl.retrieve(last_name=surname_it)}')
    bot.send_message(
        message.chat.id, f'Enter id of entry, which you want to edit')
    bot.register_next_step_handler(message, change_number)


def change_num(message):
    global number_it
    number_it = message.text
    lg.logging.info('User entered: {number_it}')
    bot.send_message(message.chat.id, f'{cl.retrieve(number=number_it)}')
    bot.send_message(
        message.chat.id, f'Enter id of entry, which you want to edit')
    bot.register_next_step_handler(message, change_number)


def change_number(message):
    global user_id_it
    user_id_it = message.text
    lg.logging.info('User entered: {user_id_it}')
    bot.send_message(
        message.chat.id, f'Enter phone number')
    bot.register_next_step_handler(message, change_new_number)


def change_new_number(message):
    global new_number_it
    new_number_it = message.text
    lg.logging.info('User entered: {new_number_it}')
    cl.update(id=user_id_it, new_number=new_number_it)
    bot.send_message(
        message.chat.id, f'Entry added successfully!')


def delete_contact(message):
    if message.text == '/71':
        lg.logging.info('The user has selected item number 7.1')
        bot.send_message(message.chat.id, f'Enter surname')
        bot.register_next_step_handler(message, delete_surname)

    elif message.text == '/72':
        lg.logging.info('The user has selected item number 7.2')
        bot.send_message(message.chat.id, f'Enter name')
        bot.register_next_step_handler(message, delete_name)

    elif message.text == '/73':
        lg.logging.info('The user has selected item number 7.3')
        bot.send_message(message.chat.id, f'Enter phone number')
        bot.register_next_step_handler(message, delete_num)

    else:
        bot.send_message(
            message.chat.id, f'I do not understand you. Enter: /help.')


def delete_surname(message):
    global surname_it
    surname_it = message.text
    lg.logging.info('User entered: {surname_it}')
    bot.send_message(message.chat.id, f'{cl.retrieve(last_name=surname_it)}')
    bot.send_message(
        message.chat.id, f'Enter id of entry, which you want to delete')
    bot.register_next_step_handler(message, delete_number)


def delete_name(message):
    global name_it
    name_it = message.text
    lg.logging.info('User entered: {name_it}')
    bot.send_message(message.chat.id, f'{cl.retrieve(name=name_it)}')
    bot.send_message(
        message.chat.id, f'Enter id of entry, which you want to delete')
    bot.register_next_step_handler(message, delete_number)


def delete_num(message):
    global number_it
    number_it = message.text
    lg.logging.info('User entered: {number_it}')
    bot.send_message(message.chat.id, f'{cl.retrieve(number=number_it)}')
    bot.send_message(
        message.chat.id, f'Enter id of entry, which you want to delete')
    bot.register_next_step_handler(message, delete_number)


def delete_number(message):
    global user_id_it
    user_id_it = message.text
    lg.logging.info('User entered: {user_id_it}')
    cl.delete(id=user_id_it)
    bot.send_message(
        message.chat.id, f'Entry successfully deleted!')


print('server start')
bot.infinity_polling()
