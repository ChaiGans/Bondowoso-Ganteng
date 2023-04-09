import random
from builtin import length, csvreader,update_csv

data_user=csvreader('user.csv')
data_bahan=csvreader('bahan_bangunan.csv')
c_jin_pengumpul = 0
pasir_terkumpul = 0
batu_terkumpul = 0
air_terkumpul = 0

# mengumpulkan bahan dengan jin pengumpul yang ada
for i in range(length(data_user)):
    if(data_user[i][2]=="jin_pengumpul"):
        c_jin_pengumpul+=1
        pasir_terkumpul+=random.randint(1, 5)
        batu_terkumpul+=random.randint(1, 5)
        air_terkumpul+=random.randint(1, 5)

# keluaran sesuai jumlah jin pengumpul
if c_jin_pengumpul>0:
    update_csv('bahan_bangunan.csv', 0, 2, int(data_bahan[0][2]) + pasir_terkumpul)
    update_csv('bahan_bangunan.csv', 1, 2, int(data_bahan[1][2]) + batu_terkumpul)
    update_csv('bahan_bangunan.csv', 2, 2, int(data_bahan[2][2]) + air_terkumpul)
    print("Mengerahkan",c_jin_pengumpul,"jin untuk mengumpulkan bahan.")
    print("Jin menemukan total",pasir_terkumpul,"pasir,",batu_terkumpul,"batu, dan",air_terkumpul,"air.")
else : print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
