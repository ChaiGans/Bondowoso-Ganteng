import builtin,tempat_variable

def login():
    # User memasukkan username atas akun yang hendak diakses
    print("Username: ", end="")
    username = str(input())

    # User memasukkan password atas username yang hendak diakses
    print("Password: ", end="")
    password = str(input())
    
    system = False # Inisialisasi return fungsi

    # Kondisi jika username ditemukan pada list data_user
    if not builtin.username_checker(username,tempat_variable.data_user):
        # Iterasi untuk menemukan posisi username pada 
        for i in range(1,tempat_variable.neff_data_user):
            if username == tempat_variable.data_user[i][0]:
                count = i # posisi "username" pada list data_user

        # Kondisi jika password sesuai dengan username yang dimasukkan pada list data_user
        if password == tempat_variable.data_user[count][1]:
            tempat_variable.nama_user= tempat_variable.data_user[count][0]
            tempat_variable.role_user= tempat_variable.data_user[count][2]
            print("Selamat datang,", str(username)+"!")
            print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
            system = True # Kondisi login berhasil

        # Kondisi jika password tidak sesuai dengan username
        else:
            print("Password Salah!")

    # Kondisi jika username tidak ditemukan pada list data_user
    else:
        print("Username tidak terdaftar!")
    
    # Jika login berhasil maka fungsi me-return username
    if system : 
        return username