import builtin,tempat_variable

# Fungsi ubahjin bertujuan untuk mengubah role daripada jin_pengumpul menjadi jin_pembangun, dan sebaliknya.
def ubahjin():

	# Meminta input username jin yang akan diubah
	print("Masukkan username jin : ", end="")
	username = str(input())

	# Kondisi jika "username" ditemukan pada list data_user
	if not builtin.username_checker (username, tempat_variable.data_user):
		# i merupakan variabel yang menyimpan posisi "username" pada list data_user
		i = builtin.find_line (tempat_variable.data_user, username) 

		# Kondisi jika role "username" pada list data_user adalah "jin_pengumpul"
		if tempat_variable.data_user[i][2] == "jin_pengumpul":

			# Meminta konfirmasi dari user untuk melakukan pengubahan role jin
			print('Jin ini bertipe "Pengumpul". Yakin ingin mengubah ke tipe "Pembangun" (Y/N)? ', end = "")
			user_input = str(input())

			system = True # Inisialisasi iterasi
			while system == True: 
				if user_input == "Y":
					tempat_variable.data_user[i][2]= "jin_pembangun"
					print("Jin telah berhasil diubah")
					system = False
				elif user_input == "N":
					print("Jin tidak jadi diubah.")
					system = False
				else: # Iterasi hingga program mendapatkan masukan yang benar
					print("Pilihan",user_input,"tidak tersedia. Sesuaikan dengan pilihan yang tersedia.")
					print('Jin ini bertipe "Pengumpul". Yakin ingin mengubah ke tipe "Pembangun" (Y/N)? ', end = "")
					user_input = str(input())

		# Kondisi jika role "username" pada list data_user adalah "jin_pembangun"
		elif tempat_variable.data_user[i][2] == "jin_pembangun":

			# Meminta konfirmasi dari user untuk melakukan pengubahan role jin
			print('Jin ini bertipe "Pembangun". Yakin ingin mengubah ke tipe "Pengumpul" (Y/N)? ', end = "")
			user_input = str(input())

			system = True # Inisialisasi iterasi
			while system == True:
				if user_input == "Y":
					tempat_variable.data_user[i][2]="jin_pengumpul"
					print("Jin telah berhasil diubah")
					system = False
				elif user_input == "N":
					print("Jin tidak jadi diubah.")
					system = False
				else: # Iterasi hingga program mendapatkan masukan yang benar
					print("Pilihan",user_input,"tidak tersedia. Sesuaikan dengan pilihan yang tersedia.")
					print('Jin ini bertipe "Pembangun". Yakin ingin mengubah ke tipe "Pengumpul" (Y/N)? ', end = "")
					user_input = str(input())

	# Kondisi jika "username" tidak ditemukan pada list data_user
	else:
		print("Tidak ada jin dengan username tersebut.")
