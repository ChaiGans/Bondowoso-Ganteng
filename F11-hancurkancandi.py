from builtin import csvreader, length

data_candi = csvreader('candi.csv')


def hancurkancandi(data_candi): 
    IDCandi = int(input("Masukkan ID Candi: ")) 
    for i in range(length(data_candi)):
        if (data_candi [i][0] == str(IDCandi)): 
             konfirmasi = input(f"Apakah anda yakin ingin menghancurkan candi ID: {IDCandi} (Y/N)?")
             if (konfirmasi == "Y" or konfirmasi == "N"):
                if (konfirmasi == "Y"): 
                    for j in range(5): 
                        data_candi[i][j] = 0
                else: 
                    print("Candi tidak jadi dihancurkan")
                    break
             else:
                print("Kode Salah")
        else:
            print("Tidak ada candi dengan ID tersebut.")
    
