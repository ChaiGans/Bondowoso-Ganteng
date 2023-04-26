import tempat_variable, builtin

# Fungsi batchkumpul bertujuan untuk memanggil seluruh jin_pengumpul untuk melakukan kumpul secara bersamaan
def batchkumpul():

    # Inisialisasi variabel
    c_jin_pengumpul = 0 # Inisialisasi count_jin_pengumpul
    pasir_total = 0
    batu_total  = 0
    air_total = 0

    # Iteraasi untuk menentukan jumlah total bahan yang dikumpulkan
    for i in range(1,tempat_variable.neff_data_user):
        # Mencari semua jin yang memiliki role jin_pengumpul
        if(tempat_variable.data_user[i][2]=="jin_pengumpul"):
            c_jin_pengumpul += 1
            tempat_variable.seed_lcg_pasir, pasir_terkumpul = builtin.lcg("kumpul", tempat_variable.seed_lcg_pasir)
            tempat_variable.seed_lcg_batu, batu_terkumpul = builtin.lcg("kumpul", tempat_variable.seed_lcg_batu)
            tempat_variable.seed_lcg_air, air_terkumpul = builtin.lcg("kumpul", tempat_variable.seed_lcg_air)
            pasir_total += pasir_terkumpul
            batu_total += batu_terkumpul
            air_total += air_terkumpul

    # Kondisi jika ditemukan jin_pengumpul pada list data_user
    # Iterasi untuk meng-update list data bahan bangunan dengan bahan bangunan yang telah dikumpulkan
    if c_jin_pengumpul>0:
        tempat_variable.data_bahanbangunan[1][2] = str(int(tempat_variable.data_bahanbangunan[1][2]) + pasir_total)
        tempat_variable.data_bahanbangunan[2][2] = str(int(tempat_variable.data_bahanbangunan[2][2]) + batu_total)
        tempat_variable.data_bahanbangunan[3][2] = str(int(tempat_variable.data_bahanbangunan[3][2]) + air_total)

        # Menampilkan pesan hasil batchkumpul
        print("Mengerahkan",c_jin_pengumpul,"jin untuk mengumpulkan bahan.")
        print("Jin menemukan total",pasir_total,"pasir,",batu_total,"batu, dan",air_total,"air.")

    # Kondisi jika tidak ditemukan jin_pengumpul dalam list data_user
    else : 
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
