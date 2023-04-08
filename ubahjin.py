from builtin import csvreader, username_checker, find_line, update_csv

data = csvreader ('user.csv')

print("Masukkan username jin : ", end="")
user_name = str(input())
if not username_checker (user_name, data):
	i = find_line (data, user_name) 
	if data[i][2] == "jin_pengumpul":
		print('Jin ini bertipe "Pengumpul". Yakin ingin mengubah ke tipe "Pembangun" (Y/N)? ', end = "")
		user_input = str(input())
		if user_input == "Y":
			update_csv('user.csv', i, 2, "jin_pembangun")
			print("Jin telah berhasil diubah")
		elif user_input == "N":
			print("Jin tidak jadi diubah.")
	elif data[i][2] == "jin_pembangun":
		print('Jin ini bertipe "Pembangun". Yakin ingin mengubah ke tipe "Pengumpul" (Y/N)? ', end = "")
		user_input = str(input())
		if user_input == "Y":
			update_csv('user.csv', i, 2, "jin_pengumpul")
			print("Jin telah berhasil diubah")
		elif user_input == "N":
			print("Jin tidak jadi diubah.")
else:
	print("Tidak ada jin dengan username tersebut.")
