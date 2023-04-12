import time,os

def save(lokasi_sumber):
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
        os.makedirs(lokasi_save)
    lokasi_save=os.path.join("save",lokasi_save)
#    if (lokasi_sumber!=lokasi_save):
        #copy aja
#    else:
        #array bacaan diawal dimasukin data dari csv di
        #lokasi_sumber

save(lokasi_sumber)