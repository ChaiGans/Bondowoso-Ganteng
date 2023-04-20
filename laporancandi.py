import tempat_variable

def laporancandi ():
    banyak_candi = pasir = batu = air = 0
    min_price = 200000
    max_price = 0
    id_termahal = "-"
    id_termurah = "-"
    for i in range(1,tempat_variable.neff_data_candi):
        if int(tempat_variable.data_candi[i][2]) != 0 and int(tempat_variable.data_candi[i][3])  != 0 and int(tempat_variable.data_candi[i][4])  != 0:
            banyak_candi += 1
            pasir += int(tempat_variable.data_candi[i][2])
            batu += int(tempat_variable.data_candi[i][3])
            air += int(tempat_variable.data_candi[i][4])
            price = int(tempat_variable.data_candi[i][2]) * 10000 + int(tempat_variable.data_candi[i][3]) * 15000 + int(tempat_variable.data_candi[i][4]) * 7500
            if price > max_price:
                max_price = price
                id_termahal = str(i)
            if price < min_price:
                min_price = price
                id_termurah = str(i)

    print(f"> Total Candi: {banyak_candi}")
    print(f"> Total Pasir yang digunakan: {pasir}")
    print(f"> Total Batu yang digunakan: {batu}")
    print(f"> Total Air yang digunakan: {air}")
    if id_termahal == '-':
        print("> ID Candi Termahal : -")
        print("> ID Candi Termurah : -")
    else:
        print(f"> ID Candi Termahal: {id_termahal + 1} (Rp {max_price})")
        print(f"> ID Candi Termurah: {id_termurah + 1} (Rp {min_price})")

