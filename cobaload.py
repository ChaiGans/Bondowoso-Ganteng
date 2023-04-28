import tempat_variable
import typing

def bukacsv (jenis, nama_lokasi : str):
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
    f=open(nama_lokasi,'r')
    isi=str(f.readline())+"*"
    i=0
    while(isi != "*"):
        titip = ""
        j=k=0
        while( j<bkanan or isi[k]!='*'):
            if(isi[k]==';'):
                print(i,j,titip)
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
    return list_dummy, neff_list_dummy
        

def bukacsv_user(nama_lokasi : str):
    f=open(nama_lokasi,'r')
    isi=str(f.readline())+"*"
    i=0
    while(isi!="*"):
        titip=""
        j=k=0
        while( j<2 or isi[k]!='*'):
            if(isi[k]==';'):
                tempat_variable.data_user[i][j]=titip
                titip=""
                j+=1
            else:
                if(isi[k]!='\n'):
                    titip+=str(isi[k])
            k+=1
        
        tempat_variable.data_user[i][j]=titip
        i+=1
        isi=f.readline()+"*"
        tempat_variable.neff_data_user=i
    f.close()

def bukacsv_candi(nama_lokasi : str):
    f=open(nama_lokasi,'r')
    isi=str(f.readline())+"*"
    i=0
    while(isi!="*"):
        titip=""
        j=k=0
        while( j<4 or isi[k]!='*'):
            if(isi[k]==';'):
                tempat_variable.data_candi[i][j]=titip
                titip=""
                j+=1
            else:
                if(isi[k]!='\n'):
                    titip+=str(isi[k])
            k+=1
        tempat_variable.data_candi[i][j]=titip
        i+=1
        isi=f.readline()+"*"
        tempat_variable.neff_data_candi=i
    f.close()

def bukacsv_bahan(nama_lokasi : str):
    f=open(nama_lokasi,'r')
    isi=str(f.readline())+"*"
    i=0
    while(isi!="*"):
        titip=""
        j=k=0
        while(isi[k]!='*'):
            if(isi[k]==';'):
                tempat_variable.data_bahanbangunan[i][j]=titip
                titip=""
                j+=1
            else:
                if(isi[k]!='\n'):
                    titip+=str(isi[k])
            k+=1
        
        tempat_variable.data_bahanbangunan[i][j]=titip
        i+=1
        isi=f.readline()+"*"
        tempat_variable.neff_data_bahanbangunan=i
    f.close()

def load():
    tempat_variable.data_user, tempat_variable.neff_data_user = bukacsv("user", tempat_variable.lokasi_file+"\\user.csv")
    tempat_variable.data_candi, tempat_variable.neff_data_candi = bukacsv("candi", tempat_variable.lokasi_file+"\\candi.csv")
    tempat_variable.data_bahanbangunan, tempat_variable.neff_data_bahanbangunan = bukacsv("bahan",tempat_variable.lokasi_file+"\\bahan_bangunan.csv")
