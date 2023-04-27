from cobasave import save

# Fungsi keluar bertujuan untuk keluar dari program, namun tetap memastikan konfirmasi user untuk melakukan penyimpanan file

def keluar():
    # Program iterasi hingga mendapatkan pilihan yang benar dari user
    input_valid = False
    while not input_valid:
        simpan_file = "Apakah Anda ingin melakukan penyimpanan file yang sudah diubah? (y/n): "
        user_simpan = input(simpan_file)

        # Kondisi jika input user "y" atau "Y" maka file akan disave pada folder yang dituju
        if user_simpan == "y" or user_simpan == "Y":
            save()
            input_valid = True

        # Kondisi jika input user "y" atau "Y maka file tidak jadi disave
        elif user_simpan == "n" or user_simpan == "N":
            input_valid = True

        # Jika user tidak memasukkan input sesuai ketentuan, maka program akan iterasi hingga mendapatkan input yang sesuai
        else:
            print("Input tidak valid. Silahkan masukkan 'y' atau 'n'")
        
    # Jika pilihan benar, maka Keluar Program