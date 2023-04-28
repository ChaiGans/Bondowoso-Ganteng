import tempat_variable
import typing


# membuka csv sesuai dengan jenis dari nama_lokasi yang diberikan
def bukacsv (jenis : str, nama_lokasi : str):

    #jenis mewakili tipe data yang akan dibaca (user/candi/bahan)
    #bkanan mewakili indeks kolom terbesar
    if jenis == "user":
        list_dummy = [["0" for i in range(3)] for j in range(113)]
        neff_list_dummy = 0
        bkanan = 2
    if jenis == "candi":
        list_dummy = [["0" for i in range(5)] for j in range(113)]
        neff_list_dummy = 0
        bkanan = 4
    if jenis == "bahan":
        list_dummy = [["0" for i in range(3)] for j in range(4)]
        neff_list_dummy = 0
        bkanan = 2

    # membuka file
    f=open(nama_lokasi,'r')
    isi=str(f.readline())+"*"
    i=0
    
    #membaca file perbaris dan memisahkannya setiap ";"
    while(isi != "*"):
        titip = ""
        j=k=0
        while( j<bkanan or isi[k]!='*'):
            if(isi[k]==';'):
                list_dummy[i][j]=titip
                titip=""
                j+=1
            else:
                if(isi[k]!='\n'):
                    titip+=str(isi[k])
            k+=1
        list_dummy[i][j] = titip
        i+=1
        isi=f.readline()+"*"
        neff_list_dummy = i
    f.close()

    # mengembalikan hasil baca
    return list_dummy, neff_list_dummy
        

def load():
    # membuka csv dan memasukkannya ke data
    tempat_variable.data_user, tempat_variable.neff_data_user = bukacsv("user", tempat_variable.lokasi_file+"\\user.csv")
    tempat_variable.data_candi, tempat_variable.neff_data_candi = bukacsv("candi", tempat_variable.lokasi_file+"\\candi.csv")
    tempat_variable.data_bahanbangunan, tempat_variable.neff_data_bahanbangunan = bukacsv("bahan",tempat_variable.lokasi_file+"\\bahan_bangunan.csv")
