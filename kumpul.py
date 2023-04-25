import builtin,tempat_variable

# Fungsi untuk jin_pengumpul mengumpulkan bahan bangunan
def kumpul():
    # Generasi angka acak dari range 1 hingga 5 dengan algoritma LCG (Linear Congruential Generator)
    pasir_kumpul = builtin.lcg()
    batu_kumpul = builtin.lcg()
    air_kumpul = builtin.lcg()

    # Menampilkan banyaknya pasir, batu, dan air yang dikumpulkan oleh jin_pengumpul
    print("Jin menemukan",pasir_kumpul, "pasir", batu_kumpul, "batu, dan", air_kumpul, "air.")

    # Meng-update list data bahan bangunan setelah melakukan pengumpulan bahan
    tempat_variable.data_bahanbangunan[1][2] = str(int(tempat_variable.data_bahanbangunan[1][2]) + pasir_kumpul)
    tempat_variable.data_bahanbangunan[2][2] = str(int(tempat_variable.data_bahanbangunan[2][2]) + batu_kumpul)
    tempat_variable.data_bahanbangunan[3][2] = str(int(tempat_variable.data_bahanbangunan[3][2]) + air_kumpul)
