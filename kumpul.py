import builtin,tempat_variable

# Fungsi untuk jin_pengumpul mengumpulkan bahan bangunan
def kumpul():
    # Generasi angka acak dari range 0 hingga 5 dengan algoritma LCG (Linear Congruential Generator)
    tempat_variable.seed_lcg_pasir, pasir_kumpul = builtin.lcg("kumpul", tempat_variable.seed_lcg_pasir)
    tempat_variable.seed_lcg_batu, batu_kumpul = builtin.lcg("kumpul", tempat_variable.seed_lcg_batu)
    tempat_variable.seed_lcg_air, air_kumpul = builtin.lcg("kumpul", tempat_variable.seed_lcg_air)

    # Menampilkan banyaknya pasir, batu, dan air yang dikumpulkan oleh jin_pengumpul
    print("Jin menemukan",pasir_kumpul, "pasir", batu_kumpul, "batu, dan", air_kumpul, "air.")

    # Meng-update list data bahan bangunan setelah melakukan pengumpulan bahan
    tempat_variable.data_bahanbangunan[1][2] = str(int(tempat_variable.data_bahanbangunan[1][2]) + pasir_kumpul)
    tempat_variable.data_bahanbangunan[2][2] = str(int(tempat_variable.data_bahanbangunan[2][2]) + batu_kumpul)
    tempat_variable.data_bahanbangunan[3][2] = str(int(tempat_variable.data_bahanbangunan[3][2]) + air_kumpul)
