import time,os,tempat_variable

def tuliscsv(jenis, tujuan, data, neff_data):
    if(jenis == "user"):
        tujuan = tujuan + "\\user.csv"
        bkanan = 2
    if(jenis == "candi"):
        tujuan = tujuan + "\\candi.csv"
        bkanan = 4
    if(jenis == "bahan"):
        tujuan = tujuan + "\\bahan_bangunan.csv"     
        bkanan = 2

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

def save():
    lokasi_save=input("Masukkan nama folder: ")
    print("Saving...")
    time.sleep(1)
    print()
    if not (os.path.isdir("save")):
        print("Membuat folder save...")
        time.sleep(1)
        os.makedirs("save")
    if not (os.path.isdir("save\\"+str(lokasi_save))):
        print("Membuat folder save/"+str(lokasi_save)+"...")
        print()
        time.sleep(1)
        os.makedirs("save\\"+lokasi_save)

    nama_folder = lokasi_save
    lokasi_save=os.path.join("save",lokasi_save)
    tuliscsv("user",lokasi_save,tempat_variable.data_user,tempat_variable.neff_data_user)
    tuliscsv("candi",lokasi_save,tempat_variable.data_candi,tempat_variable.neff_data_candi)
    tuliscsv("bahan",lokasi_save,tempat_variable.data_bahanbangunan,tempat_variable.neff_data_bahanbangunan)
   
    print("Berhasil menyimpan data di folder save/"+str(nama_folder)+" !")
