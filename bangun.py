import random
import builtin

def bangun():
# Generate a random integer between 1 and 5
	pasir_butuh = random.randint(1, 5)
	batu_butuh = random.randint(1, 5)
	air_butuh = random.randint(1, 5)

	if int(builtin.data_bahanbangunan[1][2]) >= pasir_butuh and int(builtin.data_bahanbangunan[2][2]) >= batu_butuh and int(builtin.data_bahanbangunan[3][2]) >= air_butuh:
		if builtin.length(builtin.data_candi)-1 >= 0:
			print("Candi berhasil dibangun.")
			builtin.data_candi = builtin.appendrow_candi(builtin.data_candi, builtin.length(builtin.data_candi), "user_name", pasir_butuh, batu_butuh, air_butuh)
			print("Sisa candi yang perlu dibangun: ", 101-builtin.length(builtin.data_candi))
			builtin.data_bangunan = builtin.update_list(builtin.data_bahanbangunan, 1, 2, int(builtin.data_bahanbangunan[1][2]) - pasir_butuh)
			builtin.data_bangunan = builtin.update_list(builtin.data_bahanbangunan, 2, 2, int(builtin.data_bahanbangunan[2][2]) - batu_butuh)
			builtin.data_bangunan = builtin.update_list(builtin.data_bahanbangunan, 3, 2, int(builtin.data_bahanbangunan[3][2]) - air_butuh)
		else:
			print("Candi berhasil dibangun.")
			print("Sisa candi yang perlu dibangun: ", 0)
	else:
		print("Bahan bangunan tidak mencukupi.")
		print("Candi tidak bisa dibangun!")


	builtin.cek_current_list()
