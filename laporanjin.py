# bingung nyari malas rajin nya, udah direvisi achai

from builtin import csvreader, length, appending

data_user = csvreader('user.csv')
data_candi = csvreader('candi.csv')
data_bahanbangunan = csvreader('bahan_bangunan.csv')

def jin_malas_rajin():
	list_jin_frekuensi = []
	i = 1
	while i < length(data_candi):
	    count = 1
	    j = i + 1
	    while j < length(data_candi):
	        if data_candi[i][1] == data_candi[j][1]:
	            count += 1
	        j += 1
	    list_jin_frekuensi = appending([data_candi[i][1], count], list_jin_frekuensi)
	    i += count

	frekuensi_terajin = 0
	for i in range (length(list_jin_frekuensi)):
		if list_jin_frekuensi[i][1] > frekuensi_terajin:
			frekuensi_terajin = list_jin_frekuensi[i][1]

	frekuensi_termalas = 1000
	for i in range (length(list_jin_frekuensi)):
		if list_jin_frekuensi[i][1] < frekuensi_termalas:
			frekuensi_termalas = list_jin_frekuensi[i][1]

	list_jin_rajin = []
	list_jin_malas = []
	for i in range (length(list_jin_frekuensi)):
	    if list_jin_frekuensi[i][1] == frekuensi_terajin:
	        list_jin_rajin = appending(list_jin_frekuensi[i][0], list_jin_rajin)
	    if list_jin_frekuensi[i][1] == frekuensi_termalas:
	        list_jin_malas = appending(list_jin_frekuensi[i][0], list_jin_malas)

	if length(list_jin_rajin) > 1:
	    save = list_jin_rajin[0]
	    for i in range(1, length(list_jin_rajin)):
	        if list_jin_rajin[i] < save:
	            save = list_jin_rajin[i]
	    print("Jin Terajin:", save)
	else: 
	    print("Jin Terajin:", list_jin_rajin[0])

	if length(list_jin_malas) > 1:
	    save = list_jin_malas[0]
	    for i in range(1, length(list_jin_malas)):
	        if list_jin_malas[i] > save:
	            save = list_jin_malas[i]
	    print("Jin Termalas:", save)
	else: 
	    print("Jin Termalas:", list_jin_malas[0])

jin_pembangun = 0
jin_pengumpul = 0
for i in range(1, length(data_user)):
    if data_user[i][2] == "jin_pembangun":
        jin_pembangun += 1
    elif data_user[i][2] == "jin_pengumpul":
        jin_pengumpul += 1
totaljin = jin_pembangun + jin_pengumpul

# yang ini emang cuma 3 kolom kan ya?
pasir = data_bahanbangunan [1][2]
batu = data_bahanbangunan [2][2]
air = data_bahanbangunan [3][2]

print (f"> Total Jin: {totaljin}")
print (f"> Total Jin Pengumpul: {jin_pengumpul}")
print (f"> Total Jin Pengumpul: {jin_pembangun}")
if jin_pembangun == 0:
    print(f"> Jin Terajin: -")
    print(f"> Jin Termalas: -")
else:
    jin_malas_rajin()
print(f"> Jumlah Pasir: {pasir} unit")
print(f"> Jumlah Air: {air} unit")
print(f"> Jumlah Batu: {batu} unit")

