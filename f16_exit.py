from cobasave import *

def keluar():
    input_valid = False
    while not input_valid:
        simpan_file = "Apakah Anda ingin melakukan penyimpanan file yang sudah diubah? (y/n): "
        user_simpan = input(simpan_file)

        if user_simpan == "y" or user_simpan == "Y":
            save()
            input_valid = True
        elif user_simpan == "n" or user_simpan == "N":
            input_valid = True
        else:
            print("Input tidak valid. Silahkan masukan 'y' atau 'n'")
        
# exit_program()