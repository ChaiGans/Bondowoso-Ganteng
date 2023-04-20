# Builtin function / function yang sering dipake dicopas ke sini biar tinggal dipanggil
import tempat_variable


def length(list):
    count = 0
    for x in list: #revisi. tuple
        count += 1
    return count


def appending (target,listx):
    list_dummy = listx
    list_real = [0 for i in range ((length(listx))+1)]
    for i in range (length(listx)):
        list_real[i] = list_dummy[i]
    list_real[length(listx)] = target
    return list_real

def csvreader(csv):
    with open(csv, 'r') as file:
        data = []
        row = []
        value = ''
        in_quotes = False
        for char in file.read():
            if char == ';' and not in_quotes:
                row = appending(value, row)
                value = ''
            elif char == '"' and in_quotes:
                in_quotes = False
            elif char == '"' and not in_quotes:
                in_quotes = True
            elif char != '\n':
                value += char
            else:
                row = appending(value, row)
                data = appending(row, data)
                row = []
                value = ''
        if value or row:
            row = appending(value,row)
            data = appending(row, data)
    return data


data_user = csvreader('user.csv')
data_candi = csvreader('candi.csv')
data_bahanbangunan = csvreader('bahan_bangunan.csv')

def appendrow_candi(data, idx, pembuat_candi, pasir, batu, air):
    list_dummy = [idx, pembuat_candi, pasir, batu, air]
    data = appending(list_dummy, data)
    return data

def appendrow_user(data, user_name, password, roles):
    list_dummy = [user_name, password, roles]
    data = appending(list_dummy, data)
    return data

def appendrow_bahanbangunan(data,pasir,batu,air):
    list_dummy = [pasir,batu,air]
    data = appending(list_dummy, data)
    return data

def username_checker(username, data):
    count = 0
    for i in range(length(data)):
        if data[i][0] == username:
            count += 1
    if count >= 1:
        return False
    elif count < 1:
        return True

def remove_row(data, user_name):
    count = 0
    for i in range(length(data)):
        if data[i][0] != user_name:
            count += 1
    listbaru = [0 for i in range(count)]
    count = 0
    for i in range(length(data)):
        if data[i][0] != user_name:
            listbaru[count] = data[i]
            count += 1
    return listbaru


def remove_line_csv(filename, line_number):
    with open(filename, 'r') as file:
        lines = []
        i = 0
        for line in file:
            if i != line_number:
                lines = appending (line,lines)
            i += 1

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)

def find_line (data, user_name):
    for i in range (length(data)):
        if data[i][0] == user_name:
            return i

def update_list(data, row_index, column_index, new_value):
    data[row_index][column_index] = new_value
    return data

def cek_current_list(): 
    print(data_user)
    print(data_bahanbangunan)
    print(data_candi)