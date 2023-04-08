import csv
from builtin import length
from builtin import username_checker, csvreader

data = csvreader('user.csv')
print("Username: ", end="")
username = str(input())
print("Password: ", end="")
password = str(input())

<<<<<<< HEAD
if not username_checker(username,data):
    for i in range(length(data)):
        if username == data[i][0]:
            count = i
=======
  print("Username: ", end="")
  username = str(input())
  print("Password: ", end="")
  password = str(input())
  if username_checker (username):
    for i in range (length(data)):
      if username == data[i][0]:
        count = i
>>>>>>> ef3ced06a83ad7617128b90b1d464cf6255d2f1e
    if password == data[count][1]:
        print("Selamat datang,", str(username)+"!")
        print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
    else:
        print("Password Salah!")
else:
    print("Username tidak terdaftar!")