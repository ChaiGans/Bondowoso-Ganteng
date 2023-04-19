import time,os,tempat_variable

def save():
    lokasi_save=input("Masukkan nama folder: ")
    print("Saving...")
    time.sleep(1)
    if not (os.path.isdir("save")):
        print("Membuat folder save...")
        time.sleep(1)
        os.makedirs("save")
    if not (os.path.isdir("save\\"+str(lokasi_save))):
        print("Membuat folder save/"+str(lokasi_save)+"...")
        time.sleep(1)
        os.makedirs("save\\"+lokasi_save)
    lokasi_save=os.path.join("save",lokasi_save)

    #tulis
    fw=open(lokasi_save+"\\user.csv","w")
    titip=""
    for i in range(tempat_variable.neff_data_user):
        for j in range(3):
            titip+=str(tempat_variable.data_user[i][j])
            if(j!=2):
                titip+=";"
            else: titip+="\n"
    fw.write(titip)
    fw.close()

    fw=open(lokasi_save+"\\candi.csv","w")
    titip=""
    for i in range(tempat_variable.neff_data_candi):
        for j in range(3):
            titip+=str(tempat_variable.data_candi[i][j])
            if(j!=2):
                titip+=";"
            else: titip+="\n"
    fw.write(titip)
    fw.close()

    fw=open(lokasi_save+"\\bahan_bangunan.csv","w")
    titip=""
    for i in range(tempat_variable.neff_data_bahanbangunan):
        for j in range(3):
            titip+=str(tempat_variable.data_bahanbangunan[i][j])
            if(j!=2):
                titip+=";"
            else: titip+="\n"
    fw.write(titip)
    fw.close()