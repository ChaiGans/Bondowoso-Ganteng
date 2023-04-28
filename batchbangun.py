import tempat_variable
import builtin

def batchbangun():
    c_jin_pembangun = 0
    pasir_total = 0
    batu_total = 0
    air_total = 0
    sudah_100 = False
    listbangun = [["0" for i in range(5)] for j in range(113)]
    neff_listbangun = 0
    #berisikan informasi candi jika berhasil dibangun
    #ukuran [i][4]


    # merencanakan pembangunan sesuai jumlah jin pembangun yang ada
    for i in range(1,tempat_variable.neff_data_user):
        if(tempat_variable.data_user[i][2] == "jin_pembangun"):
            c_jin_pembangun+=1

            #generate bahan yang dibutuhkan untuk bangun candi
            tempat_variable.seed_lcg_pasir, pasir_butuh = builtin.lcg("bangun", tempat_variable.seed_lcg_pasir)
            tempat_variable.seed_lcg_batu, batu_butuh = builtin.lcg("bangun", tempat_variable.seed_lcg_batu)
            tempat_variable.seed_lcg_air, air_butuh = builtin.lcg("bangun", tempat_variable.seed_lcg_air)
            pasir_total += pasir_butuh
            batu_total += batu_butuh
            air_total += air_butuh

            #jika masih ada candi yang perlu dibangun dan disimpan
            if((not sudah_100) and tempat_variable.neff_data_candi<101):

                # isi listbangun
                listbangun[neff_listbangun][1] = tempat_variable.data_user[i][0]
                listbangun[neff_listbangun][2] = str(pasir_butuh)
                listbangun[neff_listbangun][3] = str(batu_butuh)
                listbangun[neff_listbangun][4] = str(air_butuh)
                neff_listbangun+=1


                #cek jika jumlah candi sudah 100 stop
                if(tempat_variable.neff_data_candi+neff_listbangun == 101): sudah_100=True
                #101 karena ada indeks judul di data candi pusat
  
    #cek apa bisa dibangun dan beri keluaran
    if(c_jin_pembangun==0):
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")

    #ada jin dan bahan cukup
    elif (int(tempat_variable.data_bahanbangunan[1][2]) >= pasir_total and int(tempat_variable.data_bahanbangunan[2][2]) >= batu_total and int(tempat_variable.data_bahanbangunan[3][2]) >= air_total):
        #update data candi
        for i in range(neff_listbangun):
            idx_isi=tempat_variable.neff_data_candi
            listbangun[i][0]=str(builtin.carikosong())
            tempat_variable.data_candi[idx_isi] = listbangun[i]
            tempat_variable.neff_data_candi+=1


        #update sisa bahan
        tempat_variable.data_bahanbangunan[1][2]=str(int(tempat_variable.data_bahanbangunan[1][2]) - pasir_total)
        tempat_variable.data_bahanbangunan[2][2]=str(int(tempat_variable.data_bahanbangunan[2][2]) - batu_total)
        tempat_variable.data_bahanbangunan[3][2]=str(int(tempat_variable.data_bahanbangunan[3][2]) - air_total)
        
        #keluaran
        print("Mengerahkan",c_jin_pembangun,"jin untuk membangun candi dengan total bahan",pasir_total,"pasir,",batu_total,"batu, dan",air_total,"air.")
        print("Jin berhasil membangun total",c_jin_pembangun,"candi.")


    #bahan tidak cukup
    else:
        print("Mengerahkan",c_jin_pembangun," jin untuk membangun candi dengan total bahan",pasir_total,"pasir,",batu_total,"batu, dan",air_total,"air.")
        print("Bangun gagal. Kurang",end="")

        adasebelum=False #cek koma
        temp=0
        
        temp=pasir_total-int(tempat_variable.data_bahanbangunan[1][2])
        if(temp>0):
            print("",temp,"pasir",end="")
            adasebelum=True
        temp=batu_total-int(tempat_variable.data_bahanbangunan[2][2])
        if(temp>0):
            if adasebelum: print(",",end="")
            print("",temp,"batu",end="")
            adasebelum=True
        temp=air_total-int(tempat_variable.data_bahanbangunan[3][2])
        if(temp>0):
            if adasebelum: print(",",end="")
            print("",temp,"air",end="")
        print(".")