from builtin import username_checker
import tempat_variable
from F11_hancurkancandi import hancur

# Fungsi untuk menghapus jin dari list data_user dan juga menghapus candi yang pernah dibuat oleh jin tersebut
def hapusjin():
    # Meminta input username jin yang akan dihapus
    print("Masukkan username jin: ", end="")
    user_name = str(input())
    
    # Kondisi jika "user_name" berada pada list data_user dan "user_name" bukan Bondowoso dan Roro karena keduanya bukan jin
    if not username_checker(user_name, tempat_variable.data_user) and (user_name != "Bondowoso" and user_name != "Roro"):
        # Meminta konfirmasi dari user apakah benar ingin menghapus jin dengan username tersebut
        print("Apakah anda yakin ingin menghapus jin dengan username",user_name,"(Y/N)? ",end="")
        choice = str(input())
        
        # Kondisi iterasi hingga mendapatkan inputan pilihan user yang benar, yaitu "Y" atau "N"
        system = True # Inisialiasi iterasi
        while system == True:
            if choice == "Y":
                # Inisialisasi list baru untuk menyimpan data user setelah menghapus jin
                listbaru = [["0" for i in range(3)] for j in range(113)]
                count = 1
                listbaru[0] = tempat_variable.data_user[0]
                
                # Mengisi listbaru dengan komposisi list data_user kecuali jin "user_name"
                for i in range(1,tempat_variable.neff_data_user):
                    if tempat_variable.data_user[i][0] != user_name:
                        listbaru[count] = tempat_variable.data_user[i]
                        count += 1
                
                # Mengupdate neff_data_user dan data_user dengan listbaru
                tempat_variable.neff_data_user -= 1
                for i in range (1,tempat_variable.neff_data_user):
                    tempat_variable.data_user[i] = listbaru [i]
                
                # Menghapus candi yang pernah dibuat oleh jin yang dihapus
                for i in range (1,tempat_variable.neff_data_candi):
                    if (tempat_variable.data_candi[i][1] == user_name):
                        hancur(i)
                        tempat_variable.neff_data_candi -= 1
                
                # Menampilkan pesan berhasil menghapus jin dari alam gaib
                print("Jin telah berhasil dihapus dari alam gaib.")
                system = False
                
            elif choice == "N":
                # Menampilkan pesan batal menghapus jin
                print("Jin tidak jadi dihapus dari alam gaib.")
                system = False
                
            else:
                # Menampilkan pesan jika input pilihan tidak tersedia
                print("Choice",choice,"tidak tersedia. Sesuaikan dengan pilihan yang tersedia.")
                print("Apakah anda yakin ingin menghapus jin dengan username",user_name,"(Y/N)? ",end="")
                choice = str(input())
                
    # Kondisi jika "user_name" tidak ditemukan pada list data_user
    else:
        print("Tidak ada jin dengan username tersebut.")

