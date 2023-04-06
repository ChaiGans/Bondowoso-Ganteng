import csv
from builtin import length
from builtin import appendrow_user
from builtin import username_checker

def hapusjin():
    with open("./user.csv", 'r') as file:
    #https://earthly.dev/blog/csv-python/
        csvreader = csv.reader(file, delimiter = ";")
        rows = [row for row in csvreader]

    # NOTE : Masih belum ngeremove candi-candi yang dibuat sama jin
    print("Masukkan username jin: ", end="")
    user_name = str(input())

    if username_checker (user_name):
        print("Apakah anda yakin ingin menghapus jin dengan uesrname",user_name,"(Y/N)? ",end="")
        choice = str(input())
        if choice == "Y":
            print("Jin telah berhasil dihapus dari alam gaib.")
            # Remove rows where the value in column 1 is 'user_name'
            rows = [row for row in rows if row[0] != user_name]

            # Write the updated rows to the CSV file
            with open('user.csv', 'w', newline='\n') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(rows)
        elif choice == "N":
            print("Jin tidak jadi dihapus dari alam gaib.")
    else:
        print("Tidak ada jin dengan username tersebut.")