
import csv
import os.path


db_file_name = ''
db = []
global_id = 0  # id for adding entries


def init_data_base(file_name='db.csv'):
    global global_id
    global db
    global db_file_name
    db_file_name = file_name
    db.clear()
    if os.path.exists(db_file_name):
        with open(db_file_name, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if(row[0] != 'ID'):
                    db.append(row)
                    if(int(row[0]) > global_id):
                        global_id = int(row[0])
    else:
        open(db_file_name, 'w', newline='').close()


def create(name='', last_name='', number='', email=''):
    global global_id
    global db
    global db_file_name
    if(name == ''):
        print("No name specified!")
        return
    if(last_name == ''):
        print("No last name specified!")
        return
    if(number == ''):
        print("No phone number specified!")
        return
    if(email == ''):
        print("No email specified!")
        return

    for row in db:
        if(row[1] == name.title() and row[2] == last_name.title() and row[3] == number and row[4] == email.lower()):
            print("This entry already exists!")
            return

    global_id += 1
    new_row = [str(global_id), name.title(),
               last_name.title(), number, email.lower()]
    db.append(new_row)
    with open(db_file_name, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_row)


def retrieve(id='', name='', last_name='', number='', email='', format=''):
    global global_id
    global db
    global db_file_name
    result = []
    for row in db:
        if (id != '' and row[0] != id):
            continue
        if(name != '' and row[1] != name.title()):
            continue
        if(last_name != '' and row[2] != last_name.title()):
            continue
        if(number != '' and row[3] != number):
            continue
        if(email != '' and row[3] != email.lower()):
            continue
        # result.append(row)
        if(format == 1):
            result.append(", ".join(map(str, row)))
        if(format == 2):
            result.append("\n".join(map(str, row)))
    if len(result) == 0:
        return f'Contacts not found'
    else:
        # return result
        lst = "\n".join(map(str, result))
        return lst



def update(id='', new_name='', new_last_name='', new_number='', new_email=''):
    global global_id
    global db
    global db_file_name
    if(id == ''):
        print('specify id for update')
        return
    with open(db_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            if(row[0] == id):
                if(new_name != ''):
                    row[1] = new_name.title()

                if(new_last_name != ''):
                    row[2] = new_last_name.title()

                if(new_number != ''):
                    row[3] = new_number

                if(new_email != ''):
                    row[3] = new_email.lower()

            writer.writerow(row)


def delete(id=''):
    global global_id
    global db
    global db_file_name
    if(id == ''):
        print('specify id for delete')
        return

    for row in db:
        if (row[0] == id):
            db.remove(row)
            break

    with open(db_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            writer.writerow(row)


def get_token():
    file = open('token.csv', 'r')
    for i in file:
        token = i
    file.close()
    return token
