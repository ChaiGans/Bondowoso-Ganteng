import csv
from builtin import length
from builtin import username_checker

def login():
  with open("./user.csv", 'r') as file:
    #https://earthly.dev/blog/csv-python/
    csvreader = csv.reader(file, delimiter = ";")
    data = [row for row in csvreader]

  print("Username: ", end="")
  username = str(input())
  print("Password: ", end="")
  password = str(input())
  if username_checker (username):
    count = 0
    for i in range (length(data)):
      if username == data[i][0]:
        count += 1
    if password == data[count][1]:
      print("Selamat datang,", str(username)+"!")
      print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
      return True
    else:
      print("Password Salah!")
      return False
  else:
    print("Username tidak terdaftar!")
    return False
