import random,tempat_variable


def batchkumpul():
    c_jin_pengumpul = 0
    pasir_terkumpul = 0
    batu_terkumpul = 0
    air_terkumpul = 0

    # mengumpulkan bahan dengan jin pengumpul yang ada
    for i in range(1,tempat_variable.neff_data_user):
        if(tempat_variable.data_user[i][2]=="jin_pengumpul"):
            c_jin_pengumpul+=1
            pasir_terkumpul+=random.randint(1, 5)
            batu_terkumpul+=random.randint(1, 5)
            air_terkumpul+=random.randint(1, 5)

    # keluaran sesuai jumlah jin pengumpul
    if c_jin_pengumpul>0:
        tempat_variable.data_bahanbangunan[1][2] = str(int(tempat_variable.data_bahanbangunan[1][2]) + pasir_terkumpul)
        tempat_variable.data_bahanbangunan[2][2] = str(int(tempat_variable.data_bahanbangunan[2][2]) + batu_terkumpul)
        tempat_variable.data_bahanbangunan[3][2] = str(int(tempat_variable.data_bahanbangunan[3][2]) + air_terkumpul)
        print("Mengerahkan",c_jin_pengumpul,"jin untuk mengumpulkan bahan.")
        print("Jin menemukan total",pasir_terkumpul,"pasir,",batu_terkumpul,"batu, dan",air_terkumpul,"air.")
    else : print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
