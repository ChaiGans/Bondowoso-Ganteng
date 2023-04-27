import tempat_variable

# Fungsi yang bertujuan untuk menentukan pemenang, Bandung Bondowoso atau Roro Jonggrang
def ayamberkokok():    
    print("Kukuruyuk..Kukuruyuk")
    print()
    # Kondisi jika candi masih dibawah < 100 maka Roro Jonggrang menang
    if (tempat_variable.neff_data_candi < 101): 
        print("Jumlah Candi:", str((tempat_variable.neff_data_candi)-1))
        print()
        print("Selamat, Roro Jonggrang Memenangkan Permainan")
        print("")
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
        
    # Kondisi jika candi sudah 100 maka Bandung Bondowoso menang
    else: 
        print("Jumlah Candi:", tempat_variable.neff_data_candi-1)
        print()
        print("Yah, Bandung Bondowoso Memenangkan Permainan!")
    
    exit() # Keluar Program