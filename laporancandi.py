import tempat_variable

# Fungsi laporancandi bertujuan untuk menampilkan informasi-informasi tentang candi yang telah dibangun
def laporancandi ():

    # Inisialisasi nilai variabel yang digunakan pada iterasi
    banyak_candi = pasir = batu = air = 0 
    min_price = 200000
    max_price = 0
    id_termahal = "-"
    id_termurah = "-"

    # Proses iterasi
    for i in range(1,tempat_variable.neff_data_candi):
        if int(tempat_variable.data_candi[i][2]) != 0 and int(tempat_variable.data_candi[i][3]) != 0 and int(tempat_variable.data_candi[i][4]) != 0:

            # Menghitung total candi yang dibangun, pasir, batu, dan air yang digunakan
            banyak_candi += 1
            pasir += int(tempat_variable.data_candi[i][2])
            batu += int(tempat_variable.data_candi[i][3])
            air += int(tempat_variable.data_candi[i][4])

            # Menghitung harga candi dan menentukan ID candi dengan harga termahal dan termurah
            price = int(tempat_variable.data_candi[i][2]) * 10000 + int(tempat_variable.data_candi[i][3]) * 15000 + int(tempat_variable.data_candi[i][4]) * 7500
            if price > max_price:
                max_price = price
                id_termahal = tempat_variable.data_candi[i][0]
            if price < min_price:
                min_price = price
                id_termurah = tempat_variable.data_candi[i][0]

    # Menampilkan laporan candi
    print(f"> Total Candi: {banyak_candi}")
    print(f"> Total Pasir yang digunakan: {pasir}")
    print(f"> Total Batu yang digunakan: {batu}")
    print(f"> Total Air yang digunakan: {air}")

    # Menampilkan ID candi termahal dan termurah
    if id_termahal == "-":
        print("> ID Candi Termahal : -")
        print("> ID Candi Termurah : -")
    else:
        print("> ID Candi Termahal:",id_termahal,f"(Rp {max_price})")
        print("> ID Candi Termurah:",id_termurah,f"(Rp {min_price})")

