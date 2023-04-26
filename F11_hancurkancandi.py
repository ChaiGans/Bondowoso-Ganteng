import tempat_variable
import typing

# Fungsi hancur bertujuan untuk menghapus candi pada indeks tertentu
def hancur(idxhancur : int):
    for i in range(idxhancur,tempat_variable.neff_data_candi):
        tempat_variable.data_candi[i]=tempat_variable.data_candi[i+1]

# Fungsi hancurkan candi bertujuan untuk menghapus candi berdasarkan masukan ID Candi oleh user
def hancurkancandi():
    ditemukan = False # Inisialisasi dalam proses iterasi

    # Proses iterasi hingga menerima masukan ID Candi yang sesuai
    while True:
        IDCandi = input("Masukkan ID Candi: ")
        for i in range(tempat_variable.neff_data_candi):
            if tempat_variable.data_candi[i][0] == IDCandi:
                ditemukan = True # Bernilai True jika ditemukan ID Candi pada list data candi

                # Menampilkan pesan konfirmasi untuk user apakah ingin menghapus candi
                konfirmasi = input(f"Apakah anda yakin ingin menghancurkan candi ID: {IDCandi} (Y/N)?")

                system = True # Inisialisasi iterasi
                # Proses iterasi hingga mendapatkan pilihan yang sesuai dari user (Y/N)
                while system == True: 
                    if konfirmasi == "Y" or konfirmasi == "N": # Program berhenti melakukan iterasi konfirmasi jika input user Y/N
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

        # Kondisi jika ID ditemukan pada data candi sehingga program berhenti untuk melakukan iterasi
        if ditemukan:
            break
        print("Tidak ada candi dengan ID tersebut.")
