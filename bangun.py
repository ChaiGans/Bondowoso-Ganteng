import random
from builtin import csvreader, length, appendrow_candi, update_csv

# Generate a random integer between 1 and 5
pasir_butuh = random.randint(1, 5)
batu_butuh = random.randint(1, 5)
air_butuh = random.randint(1, 5)

data = csvreader('bahan_bangunan.csv')

keadaan_candi = csvreader('candi.csv')

if int(data[1][2]) >= pasir_butuh and int(data[2][2]) >= batu_butuh and int(data[3][2]) >= air_butuh:
	if length(keadaan_candi)-1 >= 0:
		print("Candi berhasil dibangun.")
		appendrow_candi(length(keadaan_candi), "user_name", pasir_butuh, batu_butuh, air_butuh)
		print("Sisa candi yang perlu dibangun: ", 101-length(keadaan_candi))
		update_csv('bahan_bangunan.csv', 1, 2, int(data[1][2]) - pasir_butuh)
		update_csv('bahan_bangunan.csv', 2, 2, int(data[2][2]) - batu_butuh)
		update_csv('bahan_bangunan.csv', 3, 2, int(data[3][2]) - air_butuh)
	else:
		print("Candi berhasil dibangun.")
		print("Sisa candi yang perlu dibangun: ", 0)
else:
	print("Bahan bangunan tidak mencukupi.")
	print("Candi tidak bisa dibangun!")