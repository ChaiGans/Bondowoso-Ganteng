import csv
def length(list):
    count = 0
    for x in  list:
        count += 1
    return count

def appendrow_user(user_name, password, roles):
    with open("./user.csv", 'a', newline='') as file:
        csvwriter = csv.writer(file, delimiter=';')
        csvwriter.writerow([user_name, password, roles])
