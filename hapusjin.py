from builtin import username_checker, remove_row, csvreader
import tempat_variable
from F11-hancurkancandi import hancur
def hapusjin():
    print("Masukkan username jin: ", end="")
    user_name = str(input())
    if not username_checker (user_name, tempat_variable.data_user):
        print("Apakah anda yakin ingin menghapus jin dengan username",user_name,"(Y/N)? ",end="")
        choice = str(input())
        if choice == "Y":
            print("Jin telah berhasil dihapus dari alam gaib.")
            count = 0
            for i in range(tempat_variable.neff_data_user):
                if tempat_variable.data_user[i][0] != user_name:
                    count += 1
            listbaru = [0 for i in range(count)]
            count = 0
            for i in range(tempat_variable.neff_data_user):
                if tempat_variable.data_user[i][0] != user_name:
                    listbaru[count] = tempat_variable.data_user[i]
                    count += 1
            for i in range (tempat_variable.neff_data_user-1):
                tempat_variable.data_user[i] = listbaru [i]
            tempat_variable.data_user[tempat_variable.neff_data_user-1] = ["0" for i in range(3)]
            for i in range (tempat_variable.neff_data_candi):
                if not username_checker (user_name, tempat_variable.data_candi):
                    hancur(i+1)
        elif choice == "N":
            print("Jin tidak jadi dihapus dari alam gaib.")
    else:
        print("Tidak ada jin dengan username tersebut.")

