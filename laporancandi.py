from builtin import csvreader

data_candi = csvreader('candi.csv')
data_user = csvreader('user.csv')
data_bahanbangunan = csvreader('bahan_bangunan.csv')

def laporancandi ():
    banyak_candi = pasir = batu = air = 0
    min_price = 200000
    max_price = 0
    id_termahal = "-"
    id_termurah = "-"
    for i in range(105):
        if data_candi[i][2] != 0 and data_candi[i][3]  != 0 and data_candi[i][4]  != 0:
            banyak_candi += 1
            pasir += data_candi[i][2]
            batu += data_candi[i][3]
            air += data_candi[i][4]
            price = data_candi[i][2] * 10000 + data_candi[i][3] * 15000 + data_candi[i][4] * 7500
            if price > max_price:
                max_price = price
                id_termahal = i
            if price < min_price:
                min_price = price
                id_termurah = i

    print(f"> Total Candi: {banyak_candi}")
    print(f"> Total Pasir yang digunakan: {pasir}")
    print(f"> Total Batu yang digunakan: {batu}")
    print(f"> Total Air yang digunakan: {air}")
    if id_termahal == '-':
        print(f"> ID Candi Termahal : -")
        print(f"> ID Candi Termurah : -")
    else:
        print(f"> ID Candi Termahal: {id_termahal + 1} (Rp {max_price})")
        print(f"> ID Candi Termurah: {id_termurah + 1} (Rp {min_price})")

