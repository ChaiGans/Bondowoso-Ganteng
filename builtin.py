import csv

with open("./user.csv", 'r') as file:
#https://earthly.dev/blog/csv-python/
    csvreader = csv.reader(file, delimiter = ";")
    data = [row for row in csvreader]

def length(list):
    count = 0
    for x in  list:
        count += 1
    return count

def appendrow_user(user_name, password, roles):
    with open("./user.csv", 'a', newline='') as file:
        csvwriter = csv.writer(file, delimiter=';')
        csvwriter.writerow([user_name, password, roles])

def username_checker (username):
    count = 0
    for i in range (length(data)):
      if data[i][0] == username:
        count += 1
    if count >= 1:
      return True
    elif count < 1: 
      return False