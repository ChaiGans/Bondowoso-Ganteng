import tempat_variable

def bukacsv_user(nama_lokasi):
    f=open(nama_lokasi,'r')
    isi=str(f.readline())+"*"
    i=0
    while(isi!="*"):
        titip=""
        j=k=0
        while(isi[k]!='*'):
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

def bukacsv_candi(nama_lokasi):
    f=open(nama_lokasi,'r')
    isi=str(f.readline())+"*"
    i=0
    while(isi!="*"):
        titip=""
        j=k=0
        while(isi[k]!='*'):
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

def bukacsv_bahan(nama_lokasi):
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
    bukacsv_user(tempat_variable.lokasi_file+"user.csv")
    bukacsv_candi(tempat_variable.lokasi_file+"candi.csv")
    bukacsv_bahan(tempat_variable.lokasi_file+"bahan_bangunan.csv")