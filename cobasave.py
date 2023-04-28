import time,os,tempat_variable

# program menulis csv di folder tujuan sesuai dengan jenis dan berisikan data
def tuliscsv(jenis : str, tujuan : str , data : list, neff_data : int):
    # membaca jenis
    if(jenis == "user"):
        tujuan = tujuan + "\\user.csv"
        bkanan = 2
    if(jenis == "candi"):
        tujuan = tujuan + "\\candi.csv"
        bkanan = 4
    if(jenis == "bahan"):
        tujuan = tujuan + "\\bahan_bangunan.csv"     
        bkanan = 2

    #menulis data perbaris
    fw = open(tujuan,"w")
    titip = ""
    for i in range(neff_data):
        for j in range(bkanan+1):
            titip += str(data[i][j])
            if(j!=bkanan):
                titip += ";"
            else: titip += "\n"
    fw.write(titip)
    fw.close()

# program save terhubung dengan program pusat
# program save mengambil masukan folder tujuan save dan menggunakan
# prosedur tuliscsv untuk menuliskan ke file
def save():

    #mengambil masukan folder tujuan save
    lokasi_save=input("Masukkan nama folder: ")
    print("Saving...")
    time.sleep(1)
    print()
    # mengecek keberadaan folder save
    # dan membuatnya jika belum ada
    if not (os.path.isdir("save")):
        print("Membuat folder save...")
        time.sleep(1)
        os.makedirs("save")
    # mengecek keberadaan folder tujuan
    # dan membuatnya jika belum ada
    if not (os.path.isdir("save\\"+str(lokasi_save))):
        print("Membuat folder save/"+str(lokasi_save)+"...")
        print()
        time.sleep(1)
        os.makedirs("save\\"+lokasi_save)

    #mengisi/mereplace file-file di folder tujuan
    nama_folder = lokasi_save
    lokasi_save=os.path.join("save",lokasi_save)
    tuliscsv("user",lokasi_save,tempat_variable.data_user,tempat_variable.neff_data_user)
    tuliscsv("candi",lokasi_save,tempat_variable.data_candi,tempat_variable.neff_data_candi)
    tuliscsv("bahan",lokasi_save,tempat_variable.data_bahanbangunan,tempat_variable.neff_data_bahanbangunan)
   
    print("Berhasil menyimpan data di folder save/"+str(nama_folder)+" !")
