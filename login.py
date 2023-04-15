import builtin

print("Username: ", end="")
username = str(input())
print("Password: ", end="")
password = str(input())

if not builtin.username_checker(username,builtin.data_user):
    for i in range(builtin.length(data)):
        if username == data[i][0]:
            count = i
    if password == data[count][1]:
        print("Selamat datang,", str(username)+"!")
        print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
    else:
        print("Password Salah!")
else:
    print("Username tidak terdaftar!")