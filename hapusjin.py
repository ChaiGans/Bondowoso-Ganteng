from builtin import username_checker
import tempat_variable
from F11_hancurkancandi import hancur

def hapusjin():
    print("Masukkan username jin: ", end="")
    user_name = str(input())
    if not username_checker (user_name, tempat_variable.data_user):
        print("Apakah anda yakin ingin menghapus jin dengan username",user_name,"(Y/N)? ",end="")
        choice = str(input())
        if choice == "Y":
            listbaru = [["0" for i in range(3)] for j in range(113)]
            count = 1
            listbaru[0]=tempat_variable.data_user[0]
            for i in range(1,tempat_variable.neff_data_user):
                if tempat_variable.data_user[i][0] != user_name:
                    listbaru[count] = tempat_variable.data_user[i]
                    count += 1
            tempat_variable.neff_data_user -= 1
            for i in range (1,tempat_variable.neff_data_user):
                tempat_variable.data_user[i] = listbaru [i]
            for i in range (1,tempat_variable.neff_data_candi):
                if (tempat_variable.data_candi[i][1]==user_name):
                    hancur(i)
                    tempat_variable.neff_data_candi -= 1
            print("Jin telah berhasil dihapus dari alam gaib.")
        elif choice == "N":
            print("Jin tidak jadi dihapus dari alam gaib.")
    else:
        print("Tidak ada jin dengan username tersebut.")

