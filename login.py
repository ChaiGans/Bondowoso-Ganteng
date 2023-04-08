import csv
from builtin import length
from builtin import username_checker, csvreader

data = csvreader('user.csv')
print("Username: ", end="")
username = str(input())
print("Password: ", end="")
password = str(input())

if not username_checker(username,data):
    for i in range(length(data)):
        if username == data[i][0]:
            count = i
    if password == data[count][1]:
        print("Selamat datang,", str(username)+"!")
        print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
    else:
        print("Password Salah!")
else:
    print("Username tidak terdaftar!")