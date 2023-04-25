import builtin
import tempat_variable

def bangun():
	# Generasi angka acak dari 1 hingga 5 dengan menerapkan konsep LCG (Linear Congruential Generator)
	pasir_butuh = builtin.lcg()
	batu_butuh = builtin.lcg()
	air_butuh = builtin.lcg()

	# Kondisi jika bahan bangunan mencukupi untuk membangun candi
	if int(tempat_variable.data_bahanbangunan[1][2]) >= pasir_butuh and int(tempat_variable.data_bahanbangunan[2][2]) >= batu_butuh and int(tempat_variable.data_bahanbangunan[3][2]) >= air_butuh:
		if tempat_variable.neff_data_candi-1 < 100:
				# Mengisi slot kosong terlebih dahulu dari list data_candi
				idx=tempat_variable.neff_data_candi
				tempat_variable.data_candi[idx][0] = str(builtin.carikosong())
				tempat_variable.data_candi[idx][1] = tempat_variable.nama_user
				tempat_variable.data_candi[idx][2] = str(pasir_butuh)
				tempat_variable.data_candi[idx][3] = str(batu_butuh)
				tempat_variable.data_candi[idx][4] = str(air_butuh)
				tempat_variable.neff_data_candi += 1

				# Data bahan bangunan akan berkurang setiap command bangun di-execute
				tempat_variable.data_bahanbangunan[1][2] = str(int(tempat_variable.data_bahanbangunan[1][2]) - pasir_butuh)
				tempat_variable.data_bahanbangunan[2][2] = str(int(tempat_variable.data_bahanbangunan[2][2])  - batu_butuh)
				tempat_variable.data_bahanbangunan[3][2] = str(int(tempat_variable.data_bahanbangunan[3][2])  - air_butuh)
				print("Candi berhasil dibangun.")
				print("Sisa candi yang perlu dibangun: ", 101 - tempat_variable.neff_data_candi)
		else: # Kondisi jika candi yang dibangun telah berjumlah 100
			print("Candi berhasil dibangun.")
			print("Sisa candi yang perlu dibangun: ", 0)
	else: # Bahan tidak cukup
		print("Bahan bangunan tidak mencukupi.")
		print("Candi tidak bisa dibangun!")
