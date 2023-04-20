from builtin import csvreader, length, appending, username_checker
import tempat_variable

def jin_malas_rajin():
	list_jin_frekuensi = [["",0] for i in range (tempat_variable.neff_data_user - 3)]
	j = 0
	for i in range (3,tempat_variable.neff_data_user):
		list_jin_frekuensi[j][0] = tempat_variable.data_user[i][0]
		j+=1

	j = 0
	count = 0
	list_jin_frekuensi_neff = 0
	while list_jin_frekuensi_neff <= tempat_variable.neff_data_user - 3:
		for i in range (tempat_variable.neff_data_candi):
			if list_jin_frekuensi[j][0] == tempat_variable.data_candi[i][1]:
				count += 1
		list_jin_frekuensi[j] = [list_jin_frekuensi[j][0], count]
		count = 0
		j += 1
		list_jin_frekuensi_neff += 1

	frekuensi_terajin = 0
	for i in range (list_jin_frekuensi_neff):
		if list_jin_frekuensi[i][1] > frekuensi_terajin:
			frekuensi_terajin = list_jin_frekuensi[i][1]

	frekuensi_termalas = 1000
	for i in range (list_jin_frekuensi_neff):
		if list_jin_frekuensi[i][1] < frekuensi_termalas:
			frekuensi_termalas = list_jin_frekuensi[i][1]

	list_jin_rajin_neff = 0
	list_jin_malas_neff = 0
	for i in range (list_jin_frekuensi_neff):
	    if list_jin_frekuensi[i][1] == frekuensi_terajin:
			list_jin_rajin_neff += 1
	    if list_jin_frekuensi[i][1] == frekuensi_termalas:
			list_jin_malas_neff += 1

	list_jin_rajin = ["" for i in range (list_jin_rajin_neff)]
	list_jin_malas = ["" for i in range (list_jin_malas_neff)]

	j=0
	k=0
	for i in range (list_jin_frekuensi_neff):
		if list_jin_frekuensi[i][1] == frekuensi_terajin:
			list_jin_rajin[j] = list_jin_frekuensi[i][0]
			j+=1
		if list_jin_frekuensi[i][1] == frekuensi_termalas:
			list_jin_malas[k] = list_jin_frekuensi[i][0]
			k+=1

	if list_jin_rajin_neff > 1:
	    save = list_jin_rajin[0]
	    for i in range(1, list_jin_rajin_neff):
	        if list_jin_rajin[i] < save:
	            save = list_jin_rajin[i]
	    print("Jin Terajin:", save)
	else: 
	    print("Jin Terajin:", list_jin_rajin[0])

	if list_jin_malas_neff > 1:
	    save = list_jin_malas[0]
	    for i in range(1, list_jin_malas_neff):
	        if list_jin_malas[i] > save:
	            save = list_jin_malas[i]
	    print("Jin Termalas:", save)
	else: 
	    print("Jin Termalas:", list_jin_malas[0])

jin_pembangun = 0
jin_pengumpul = 0
for i in range(1, tempat_variable.neff_data_user):
    if data_user[i][2] == "jin_pembangun":
        jin_pembangun += 1
    elif data_user[i][2] == "jin_pengumpul":
        jin_pengumpul += 1
totaljin = jin_pembangun + jin_pengumpul

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


