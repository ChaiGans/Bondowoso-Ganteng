import random
import builtin
import tempat_variable

def bangun():
	# Generate a random integer between 1 and 5
	pasir_butuh = random.randint(1, 5)
	batu_butuh = random.randint(1, 5)
	air_butuh = random.randint(1, 5)

	if int(tempat_variable.data_bahanbangunan[1][2]) >= pasir_butuh and int(tempat_variable.data_bahanbangunan[2][2]) >= batu_butuh and int(tempat_variable.data_bahanbangunan[3][2]) >= air_butuh:
		if tempat_variable.neff_data_candi-1 < 100:
				idx=tempat_variable.neff_data_candi
				tempat_variable.data_candi[idx][0] = str(builtin.carikosong())
				tempat_variable.data_candi[idx][1] = tempat_variable.nama_user
				tempat_variable.data_candi[idx][2] = str(pasir_butuh)
				tempat_variable.data_candi[idx][3] = str(batu_butuh)
				tempat_variable.data_candi[idx][4] = str(air_butuh)
				tempat_variable.neff_data_candi += 1
				tempat_variable.data_bahanbangunan[1][2] = str(int(tempat_variable.data_bahanbangunan[1][2]) - pasir_butuh)
				tempat_variable.data_bahanbangunan[2][2] = str(int(tempat_variable.data_bahanbangunan[2][2])  - batu_butuh)
				tempat_variable.data_bahanbangunan[3][2] = str(int(tempat_variable.data_bahanbangunan[3][2])  - air_butuh)
				print("Candi berhasil dibangun.")
				print("Sisa candi yang perlu dibangun: ", 101 - tempat_variable.neff_data_candi)
		else:
			print("Candi berhasil dibangun.")
			print("Sisa candi yang perlu dibangun: ", 0)
	else:
		print("Bahan bangunan tidak mencukupi.")
		print("Candi tidak bisa dibangun!")
