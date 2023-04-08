import csv
from builtin import length
from builtin import appendrow_user
from builtin import username_checker, remove_line_csv, find_line, csvreader

data = csvreader('user.csv')

# NOTE : Masih belum ngeremove candi-candi yang dibuat sama jin
print("Masukkan username jin: ", end="")
user_name = str(input())

if not username_checker (user_name, data):
    print("Apakah anda yakin ingin menghapus jin dengan uesrname",user_name,"(Y/N)? ",end="")
    choice = str(input())
    if choice == "Y":
        print("Jin telah berhasil dihapus dari alam gaib.")
        line_number = find_line (data, user_name)
        remove_line_csv('user.csv',line_number)
    elif choice == "N":
        print("Jin tidak jadi dihapus dari alam gaib.")
else:
    print("Tidak ada jin dengan username tersebut.")