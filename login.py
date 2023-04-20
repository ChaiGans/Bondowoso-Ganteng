import builtin,tempat_variable

print("Username: ", end="")
username = str(input())
print("Password: ", end="")
password = str(input())

if not builtin.username_checker(username,tempat_variable.data_user):
    for i in range(1,tempat_variable.neff_data_user):
        if username == tempat_variable.data_user[i][0]:
            count = i
    if password == tempat_variable.data_user[count][1]:
        print("Selamat datang,", str(username)+"!")
        print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
    else:
        print("Password Salah!")
else:
    print("Username tidak terdaftar!")