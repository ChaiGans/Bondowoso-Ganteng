import random
import builtin
import tempat_variable

def bangun():
	# Generate a random integer between 1 and 5
	pasir_butuh = random.randint(1, 5)
	batu_butuh = random.randint(1, 5)
	air_butuh = random.randint(1, 5)

	if int(tempat_variable.data_bahanbangunan[1][2]) >= pasir_butuh and int(tempat_variable.data_bahanbangunan[2][2]) >= batu_butuh and int(tempat_variable.data_bahanbangunan[3][2]) >= air_butuh:
		if tempat_variable.neff_data_candi-1 <= 100:
			print("Candi berhasil dibangun.")
			for i in range (tempat_variable.neff_data_candi):
				if tempat_variable.data_candi[i][2]==0 and tempat_variable.data_candi[i][3]==0 and tempat_variable.data_candi[i][4]==0:
					tempat_variable.data_candi[i][2] = pasir_butuh
					tempat_variable.data_candi[i][3] = batu_butuh
					tempat_variable.data_candi[i][4] = air_butuh
					print("Sisa candi yang perlu dibangun: ", 100-tempat_variable.neff_data_candi)
				else:
					break
		else:
			print("Candi berhasil dibangun.")
			print("Sisa candi yang perlu dibangun: ", 0)
	else:
		print("Bahan bangunan tidak mencukupi.")
		print("Candi tidak bisa dibangun!")
