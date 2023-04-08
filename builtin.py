# Builtin function / function yang sering dipake dicopas ke sini biar tinggal dipanggil

def length(list):
    count = 0
    for x in list:
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

def appendrow_candi(idx, pembuat_candi, pasir, batu, air):
    with open('candi.csv', 'a') as file:
        file.write('{};{};{};{};{}\n'.format(idx, pembuat_candi, pasir, batu, air))

def appendrow_user(user_name, password, roles):
    with open('user.csv', 'a') as file:
        file.write('{};{};{}\n'.format(user_name, password, roles))

def appendrow_bahanbangunan(pasir,batu,air):
    with open('user.csv', 'a') as file:
        file.write('{};{};{}\n'.format(pasir, batu, air))

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
    listbaru = [0 for i in range(length(data) - 1)]
    count = 0
    for i in range(length(data)):
        if data[i][0] == user_name:
            continue
        else:
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

def update_csv(filename, row_index, column_index, new_value):
    data = csvreader (filename)
    data[row_index][column_index] = new_value

    with open(filename, 'w') as file:
        for row in data:
            line = ''
            for i in range(length (row)):
                line += str(row[i])
                if i != length (row) - 1:
                    line += ';'
            file.write(line + '\n')