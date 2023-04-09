import random
from builtin import length, csvreader,update_csv,appendrow_candi

data_user=csvreader('user.csv')
data_bahan=csvreader('bahan_bangunan.csv')
data_candi=csvreader('candi.csv')
c_jin_pembangun = 0
pasir_total = 0
batu_total = 0
air_total = 0
sudah_100=False
listbangun=[]
#berisikan informasi candi jika berhasil dibangun
#ukuran [i][4]


# merencanakan pembangunan sesuai jumlah jin pembangun yang ada
for i in range(length(data_user)):
    if(data_user[i][2]=="jin_pembangun"):
        c_jin_pembangun+=1
        
        #jika masih ada candi yang perlu dibangun
        if(not sudah_100 and length(data_candi)<100):

            #generate bahan yang dibutuhkan
            pasir_butuh=random.randint(1, 5)
            batu_butuh=random.randint(1, 5)
            air_butuh=random.randint(1, 5)
            pasir_total+=pasir_butuh
            batu_total+=batu_butuh
            air_total+=air_butuh

            # append listbangun
            titiplist=listbangun
            llist=length(titiplist)
            listbangun=[[0 for j in range (4)]for k in range(llist+1)]
            for j in range(llist):
                for k in range(0,4):
                    listbangun[j][k]=titiplist[j][k]
            listbangun[llist][0]=data_user[i][0]
            listbangun[llist][1]=pasir_butuh
            listbangun[llist][2]=batu_butuh
            listbangun[llist][3]=air_butuh

            #cek jika jumlah candi sudah 100 stop
            if(length(data_candi)+llist+1==100): sudah_100=True

#cek apa bisa dibangun dan beri keluaran
if(c_jin_pembangun==0):
    print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")

elif (int(data_bahan[0][2]) >= pasir_total and data_bahan[1][2] >= batu_total and data_bahan[2][2] >= air_total):
    #update data candi
    for i in range(llist+1):
        appendrow_candi(length(data_candi), listbangun[i][0], listbangun[i][1], listbangun[i][2], listbangun[i][3])

    #update sisa bahan
    update_csv('bahan_bangunan.csv', 0, 2, int(data_bahan[0][2]) - pasir_total)
    update_csv('bahan_bangunan.csv', 1, 2, int(data_bahan[1][2]) - batu_total)
    update_csv('bahan_bangunan.csv', 2, 2, int(data_bahan[2][2]) - air_total)
    
    #keluaran
    print("Mengerahkan",c_jin_pembangun," jin untuk membangun candi dengan total bahan",pasir_total,"pasir,",batu_total,"batu, dan",air_total,"air.")
    print("Jin berhasil membangun total",llist+1,"candi.")

    #KELUARAN JIKA JUMLAH JIN DAN JUMLAH CANDI DIBANGUN TIDAK SAMA KARENA MELEBIHI 100
    #BELUM

else:
    print("Mengerahkan 22 jin untuk membangun candi dengan total bahan 71 pasir, 89 batu, dan 95 air.")
    print("Bangun gagal. Kurang",end="")

    adasebelum=False #cek koma

    if((pasir_total-data_bahan[0][2])>0):
        print(pasir_total-data_bahan[0][2]," pasir",end="")
        adasebelum=True
    if((batu_total-data_bahan[1][2])>0):
        if adasebelum: print(",",end="")
        print(batu_total-data_bahan[1][2]," batu",end="")
        adasebelum=True
    if((air_total-data_bahan[2][2])>0):
        if adasebelum: print(",",end="")
        print(air_total-data_bahan[2][2]," air",end="")
    print(".")