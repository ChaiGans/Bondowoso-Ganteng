import tempat_variable

def hancurkancandi():
    #array belum dimundurin
    #mundurin : geser array, ubah neff
    ditemukan=False
    IDCandi = int(input("Masukkan ID Candi: ")) 
    for i in range(tempat_variable.neff_data_candi):
        if (tempat_variable.data_candi[i][0] == str(IDCandi)):
            ditemukan=True
            konfirmasi = input(f"Apakah anda yakin ingin menghancurkan candi ID: {IDCandi} (Y/N)?")
            if (konfirmasi == "Y" or konfirmasi == "N"):
                if (konfirmasi == "Y"): 
                    for j in range(5): 
                        tempat_variable.data_candi[i][j] = "0"
                else: 
                    print("Candi tidak jadi dihancurkan")
                    break
            else:
                print("Kode Salah")
    if ditemukan==False :
        print("Tidak ada candi dengan ID tersebut.")
    
