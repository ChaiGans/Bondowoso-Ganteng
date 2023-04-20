import builtin,tempat_variable

def ubahjin():
	print("Masukkan username jin : ", end="")
	user_name = str(input())
	if not builtin.username_checker (user_name, tempat_variable.data_user):
		i = builtin.find_line (tempat_variable.data_user, user_name) 
		if builtin.data_user[i][2] == "jin_pengumpul":
			print('Jin ini bertipe "Pengumpul". Yakin ingin mengubah ke tipe "Pembangun" (Y/N)? ', end = "")
			user_input = str(input())
			if user_input == "Y":
				tempat_variable.data_user[i][2]= "jin_pembangun"
				print("Jin telah berhasil diubah")
			elif user_input == "N":
				print("Jin tidak jadi diubah.")
		elif builtin.data_user[i][2] == "jin_pembangun":
			print('Jin ini bertipe "Pembangun". Yakin ingin mengubah ke tipe "Pengumpul" (Y/N)? ', end = "")
			user_input = str(input())
			if user_input == "Y":
				tempat_variable.data_user[i][2]="jin_pengumpul"
				print("Jin telah berhasil diubah")
			elif user_input == "N":
				print("Jin tidak jadi diubah.")
	else:
		print("Tidak ada jin dengan username tersebut.")
