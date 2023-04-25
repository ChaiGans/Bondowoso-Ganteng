import tempat_variable

def hancur(idxhancur):
    for i in range(idxhancur,tempat_variable.neff_data_candi):
        tempat_variable.data_candi[i]=tempat_variable.data_candi[i+1]


def hancurkancandi():
    ditemukan = False
    while True:
        IDCandi = input("Masukkan ID Candi: ")
        for i in range(tempat_variable.neff_data_candi):
            if tempat_variable.data_candi[i][0] == IDCandi:
                ditemukan = True
                konfirmasi = input(f"Apakah anda yakin ingin menghancurkan candi ID: {IDCandi} (Y/N)?")
                system = True
                while system == True:
                    if konfirmasi == "Y" or konfirmasi == "N":
                        if konfirmasi == "Y": 
                            hancur(i)
                            tempat_variable.neff_data_candi -= 1
                            print("Candi dengan ID", IDCandi, "berhasil dihancurkan")
                            system = False
                        else: 
                            print("Candi tidak jadi dihancurkan")
                            system = False
                    else:
                        print("Pilihan", konfirmasi, "tidak tersedia. Silahkan masukkan pilihan yang sesuai.")
                        konfirmasi = input(f"Apakah anda yakin ingin menghancurkan candi ID: {IDCandi} (Y/N)?")
                break
        if ditemukan:
            break
        print("Tidak ada candi dengan ID tersebut.")
