# nyerah nyari malas rajin


from builtin import csvreader

data_user = csvreader('user.csv')
data_candi = csvreader('candi.csv')
data_bahanbangunan = csvreader('bahan_bangunan.csv')

def rajin (jin1,jin2):
    if (jin1).lower() < (jin2).lower():
        return (jin1)
    elif (jin1).lower() > (jin2).lower():
        return (jin2)

def malas (jin1,jin2):
    if (jin1).lower() > (jin2).lower():
        return (jin1)
    elif (jin1).lower() < (jin2).lower():
        return (jin2)

jin = 0
jin_pembangun = 0
jin_pengumpul = 0
for i in range (1000):
    if data_user [i][2] == "jin_pembangun":
        jin_pembangun += 1
    elif data_user [i][2] == "jin_pengumpul":
        jin_pengumpul += 1
totaljin = jin_pembangun + jin_pengumpul

pasir = data_bahanbangunan [1][2]
batu = data_bahanbangunan [2][2]
air = data_bahanbangunan [3][2]

print (f"> Total Jin: {totaljin}")
print(f"> Total Jin Pengumpul: {jin_pengumpul}")
print{f"> Total Jin Pengumpul: {jin_pembangun}"}
if jin_pembangun == 0:
    print(f"> Jin Terajin: -")
    print(f"> Jin Termalas: -")
else:
    print(f"> Jin Terajin: {}")
    print(f"> Jin Termalas: {}")
print(f"> Jumlah Pasir: {pasir} unit")
print(f"> Jumlah Air: {air} unit")
print(f"> Jumlah Batu: {batu} unit")

