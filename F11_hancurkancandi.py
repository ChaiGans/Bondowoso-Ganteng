import tempat_variable

def hancur(idxhancur):
    for i in range(idxhancur,tempat_variable.neff_data_candi):
        tempat_variable.data_candi[i]=tempat_variable.data_candi[i+1]


def hancurkancandi():
    ditemukan=False
    IDCandi = int(input("Masukkan ID Candi: ")) 
    for i in range(tempat_variable.neff_data_candi):
        if (tempat_variable.data_candi[i][0] == str(IDCandi)):
            ditemukan=True
            konfirmasi = input(f"Apakah anda yakin ingin menghancurkan candi ID: {IDCandi} (Y/N)?")
            if (konfirmasi == "Y" or konfirmasi == "N"):
                if (konfirmasi == "Y"): 
                    hancur(i)
                    tempat_variable.neff_data_candi-=1
                else: 
                    print("Candi tidak jadi dihancurkan")
                    break
            else:
                print("Kode Salah")
    if ditemukan == False :
        print("Tidak ada candi dengan ID tersebut.")