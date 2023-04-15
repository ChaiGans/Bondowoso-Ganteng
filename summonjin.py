import builtin

def summonjin():
    if builtin.length(builtin.data_user)-1 == 100:
        print ("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu.")
    else:
        print("Jenis jin yang dapat dipanggil: ")
        print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("(2) Pembangun - Bertugas membangun candi")
        print()
        print("Masukkan nomor jenis jin yang ingin dipanggil: ", end="")
        jenis_jin = int(input())
        while (jenis_jin != 1 and jenis_jin != 2):
            print('Tidak ada jenis jin bernomor "'+str(jenis_jin)+'"!')
            print("Masukkan nomor jenis jin yang ingin dipanggil: ", end="")
            jenis_jin = int(input())
        if jenis_jin == 1:
            print('Memilih jin "Pengumpul"')
            print("Masukkan username jin: ", end="")
            user_name = str(input())
            while not builtin.username_checker (user_name,builtin.data_user):
                print('Username "'+str(user_name)+'" sudah diambil!')
                print("Masukkan username jin: ", end="")
                user_name = str(input())

            print("Masukkan password jin: ", end ="")
            password_input = str(input())
            while builtin.length(password_input) < 5 or builtin.length(password_input) > 25:
                print("Password panjangnya harus 5-25 karakter!")
                print("Masukkan password jin: ", end ="")
                password_input = str(input())
            
            print("Mengumpulkan sesajen...")
            print("Menyerahkan sesajen...")
            print("Membacakan mantra...")
            print("Jin",user_name,"berhasil dipanggil!")

            builtin.data_user = builtin.appendrow_user(builtin.data_user, user_name, password_input, "jin_pengumpul")

        elif jenis_jin == 2:
            print('Memilih jin "Pembangun"')
            print("Masukkan username jin: ", end="")
            user_name = str(input())
            while not builtin.username_checker (user_name,builtin.data_user):
                print('Username "'+str(user_name)+'" sudah diambil!')
                print("Masukkan username jin: ", end="")
                user_name = str(input())

            print("Masukkan password jin: ", end ="")
            password_input = str(input())
            while builtin.length(password_input) < 5 or builtin.length(password_input) > 25:
                print("Password panjangnya harus 5-25 karakter!")
                print("Masukkan password jin: ", end ="")
                password_input = str(input())
            
            print("Mengumpulkan sesajen...")
            print("Menyerahkan sesajen...")
            print("Membacakan mantra...")
            print("Jin",user_name,"berhasil dipanggil!")

            builtin.data_user = builtin.appendrow_user(builtin.data_user, user_name, password_input, "jin_pembangun")
    
    builtin.cek_current_list()


