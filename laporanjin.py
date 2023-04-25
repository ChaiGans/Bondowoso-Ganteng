import tempat_variable

def jin_malas_rajin():
    # Inisialisasi list untuk menyimpan komposisi [nama_jin, frekuensi]
    list_jin_frekuensi = [["", 0] for i in range(tempat_variable.neff_data_user - 3)]

    # Inisialisasi variabel iterasi
    j = 0
    list_jin_frekuensi_neff = 0 # Panjang list jin frekuensi yang terisi

    # Mengisi list jin frekuensi dengan nama jin yang terdapat pada list data user
    for i in range(3, tempat_variable.neff_data_user):
        list_jin_frekuensi[j][0] = tempat_variable.data_user[i][0]
        j += 1
        list_jin_frekuensi_neff += 1

    # Menghitung banyak ['', 0] pada list jin frekuensi
    count = 0
    for i in range(list_jin_frekuensi_neff):
        if list_jin_frekuensi[i] == ['',0]:
            count += 1

    # Memindahkan isi list jin frekuensi ke list jin frekuensi baru yang bersih tanpa ['', 0]
    list_jin_frekuensi_baru = [["", 0] for i in range(list_jin_frekuensi_neff-count)]
    list_jin_frekuensi_baru_neff = 0
    j = 0
    for i in range (list_jin_frekuensi_neff):
        if list_jin_frekuensi[i] != ['',0]: 
            list_jin_frekuensi_baru[j] = list_jin_frekuensi[i]
            j+=1
            list_jin_frekuensi_baru_neff = list_jin_frekuensi_baru_neff + 1

    # Inisialisasi variabel iterasi
    j = 0
    count = 0
    # Iterasi untuk menghasilkan list_jin_frekuensi_baru dengan format [nama_jin, frekuensi]
    # frekuensi merupakan Frekuensi muncul nama jin pada list data candi
    while j <= (list_jin_frekuensi_baru_neff-1):
        for i in range(1,tempat_variable.neff_data_candi):
            if list_jin_frekuensi_baru[j][0] == tempat_variable.data_candi[i][1]:
                count += 1
        list_jin_frekuensi_baru[j] = [list_jin_frekuensi_baru[j][0], count]
        count = 0
        j += 1

    # Mencari frekuensi terajin dari list_jin_frekuensi_baru
    frekuensi_terajin = 0
    for i in range(list_jin_frekuensi_baru_neff):
        if list_jin_frekuensi_baru[i][1] > frekuensi_terajin:
            frekuensi_terajin = list_jin_frekuensi_baru[i][1]

    # Mencari frekuensi termalas dari list_jin_frekuensi_baru
    frekuensi_termalas = 1000
    for i in range(list_jin_frekuensi_baru_neff):
        if list_jin_frekuensi_baru[i][1] < frekuensi_termalas:
            frekuensi_termalas = list_jin_frekuensi_baru[i][1]

    # Inisalisasi panjang list_jin_rajin dan list_jin_malas
    list_jin_rajin_neff = 0
    list_jin_malas_neff = 0


    # Menghitung panjang list untuk menampun jin terajin dan termalas
    for i in range(list_jin_frekuensi_baru_neff):
        if list_jin_frekuensi_baru[i][1] == frekuensi_terajin:
            list_jin_rajin_neff += 1
        if list_jin_frekuensi_baru[i][1] == frekuensi_termalas:
            list_jin_malas_neff += 1

    # Inisialisasi list_jin_rajin dan list_jin_malas untuk menampung nama jin terajin dan termalas
    list_jin_rajin = ["" for i in range(list_jin_rajin_neff)]
    list_jin_malas = ["" for i in range(list_jin_malas_neff)]

    # Inisalisasi variabel iterasi
    j = 0
    k = 0

    # Iterasi untuk memasukkan nama jin terajin dan termalas ke list masing-masing
    for i in range(list_jin_frekuensi_baru_neff):
        if list_jin_frekuensi_baru[i][1] == frekuensi_terajin:
            list_jin_rajin[j] = list_jin_frekuensi_baru[i][0]
            j += 1
        if list_jin_frekuensi_baru[i][1] == frekuensi_termalas:
            list_jin_malas[k] = list_jin_frekuensi_baru[i][0]
            k += 1

    # Iterasi untuk mencari jin terajin dengan leksikografis terendah
    if list_jin_rajin_neff > 0:
        save = list_jin_rajin[0]
        for i in range(1, list_jin_rajin_neff):
            # Mencari leksikografis terendah
            if list_jin_rajin[i] < save: 
                save = list_jin_rajin[i]      
        # Menampilkan pesan jin terajin
        print("> Jin Terajin:", save)

    # Iterasi untuk mencari jin termalas dengan leksikografis tertinggi
    if list_jin_malas_neff > 0:
        save = list_jin_malas[0]
        for i in range(1, list_jin_malas_neff):
            # Mencari leksikografis tertinggi
            if list_jin_malas[i] > save:
                save = list_jin_malas[i]
        # Menampilkan pesan jin termalas
        print("> Jin Termalas:", save)

# Fungsi laporanjin bertujuan untuk memberikan laporan tentang kinerja daripada jin
def laporanjin():
    # Inisialisasi variabel banyak jin
    jin_pembangun = 0
    jin_pengumpul = 0

    # Iterasi untuk menghitung banyak jin_pembangun dan jin_pengumpul
    for i in range(1, tempat_variable.neff_data_user):
        if tempat_variable.data_user[i][2] == "jin_pembangun":
            jin_pembangun += 1
        elif tempat_variable.data_user[i][2] == "jin_pengumpul":
            jin_pengumpul += 1

    # Total jin merupakan penjumlahan antara jin_pembangun dan jin_pengumpul
    totaljin = jin_pembangun + jin_pengumpul

    # Memanggil bahan pasir, batu, dan air dari file tempat_variable
    pasir = tempat_variable.data_bahanbangunan [1][2]
    batu = tempat_variable.data_bahanbangunan [2][2]
    air = tempat_variable.data_bahanbangunan [3][2]

    # Pesan keluaran yang menampilkan laporan jin
    print (f"> Total Jin: {totaljin}")
    print (f"> Total Jin Pengumpul: {jin_pengumpul}")
    print (f"> Total Jin Pembangun: {jin_pembangun}")
    if jin_pembangun == 0 and jin_pengumpul == 0:
        print(f"> Jin Terajin: -")
        print(f"> Jin Termalas: -")
    else:
        # Memanggil kembali fungsi jin_malas_rajin yang telah dibuat sebelumnya
        jin_malas_rajin()
    print(f"> Jumlah Pasir: {pasir} unit")
    print(f"> Jumlah Air: {air} unit")
    print(f"> Jumlah Batu: {batu} unit")


