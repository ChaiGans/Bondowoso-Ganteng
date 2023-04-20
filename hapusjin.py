import builtin,tempat_variable

def hapusjin():
    # NOTE : Masih belum ngeremove candi-candi yang dibuat sama jin
    print("Masukkan username jin: ", end="")
    user_name = str(input())

    if not builtin.username_checker (user_name, tempat_variable.data_user):
        print("Apakah anda yakin ingin menghapus jin dengan username",user_name,"(Y/N)? ",end="")
        choice = str(input())
        if choice == "Y":
            print("Jin telah berhasil dihapus dari alam gaib.")
            builtin.data_user = builtin.remove_row(builtin.data_user,user_name)
            for i in range (length(builtin.data_candi)):
                if not builtin.username_checker (user_name, builtin.data_candi):
                    builtin.data_candi[i][1] = "0"
                    builtin.data_candi[i][2] = 0
                    builtin.data_candi[i][3] = 0
                    builtin.data_candi[i][4] = 0
        elif choice == "N":
            print("Jin tidak jadi dihapus dari alam gaib.")
    else:
        print("Tidak ada jin dengan username tersebut.")

    builtin.cek_current_list()

