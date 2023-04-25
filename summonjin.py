import builtin,tempat_variable

def summonjin():
    # Kondisi jika panjang list data_user sudah mencapai batas maksimal yaitu 103 (1 Deskripsi, 1 Bondowoso, dan 1 Roro)
    if tempat_variable.neff_data_user-1 == 102:
        print ("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu.")

    # Kondisi jika jumlah jin masih dibawah 100
    else:
        # Menampilkan pesan jenis jin yang dapat dipanggil
        print("Jenis jin yang dapat dipanggil: ")
        print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("(2) Pembangun - Bertugas membangun candi")
        print()

        # Meminta masukan dari pengguna jenis jin yang ingin dipanggil
        print("Masukkan nomor jenis jin yang ingin dipanggil: ", end="")
        jenis_jin = input()

        # Iterasi jika masukan pengguna tidak sesuai dengan spesifikasi
        while (jenis_jin != "1" and jenis_jin != "2"):
            print('Tidak ada jenis jin bernomor "'+str(jenis_jin)+'"!')
            print("Masukkan nomor jenis jin yang ingin dipanggil: ", end="")
            jenis_jin = int(input())

        # Kondisi jika pengguna memilih summon jin_pengumpul
        if jenis_jin == "1":
            # Meminta inputan user atas username jin yang hendak di-summon
            print('Memilih jin "Pengumpul"')
            print("Masukkan username jin: ", end="")
            user_name = str(input())

            # Jika nama sudah ada di list data_user, maka pengguna harus memasukkan nama lain yang unik
            while not builtin.username_checker (user_name,tempat_variable.data_user):
                print('Username "'+str(user_name)+'" sudah diambil!')
                print("Masukkan username jin: ", end="")
                user_name = str(input())

            # Jika nama jin sudah unik, program meminta inputan password dari user
            print("Masukkan password jin: ", end ="")
            password_input = str(input())

            # Iterasi masukan "password" oleh user hingga memenuhi spesifikasi yaitu panjang password 5-25 karakter
            while builtin.lengthstring(password_input) < 5 or builtin.lengthstring(password_input) > 25:
                print("Password panjangnya harus 5-25 karakter!")
                print("Masukkan password jin: ", end ="")
                password_input = str(input())
            
            # Menampilkan pesan keberhasilan pemanggilan jin / summon jin
            print("Mengumpulkan sesajen...")
            print("Menyerahkan sesajen...")
            print("Membacakan mantra...")
            print("Jin",user_name,"berhasil dipanggil!")

            # Menambahkan pasang username, password, dan role jin ke dalam list data_user
            builtin.appendrow_user(user_name, password_input, "jin_pengumpul")

        # Kondisi jika pengguna memilih summon jin_pembangun
        elif jenis_jin == "2":
            # Meminta inputan user atas username jin yang hendak di-summon
            print('Memilih jin "Pembangun"')
            print("Masukkan username jin: ", end="")
            user_name = str(input())

            # Jika nama sudah ada di list data_user, maka pengguna harus memasukkan nama lain yang unik
            while not builtin.username_checker (user_name,tempat_variable.data_user):
                print('Username "'+str(user_name)+'" sudah diambil!')
                print("Masukkan username jin: ", end="")
                user_name = str(input())

            # Jika nama jin sudah unik, program meminta inputan password dari user
            print("Masukkan password jin: ", end ="")
            password_input = str(input())

            # Iterasi masukan "password" oleh user hingga memenuhi spesifikasi yaitu panjang password 5-25 karakter
            while builtin.lengthstring(password_input) < 5 or builtin.lengthstring(password_input) > 25:
                print("Password panjangnya harus 5-25 karakter!")
                print("Masukkan password jin: ", end ="")
                password_input = str(input())
            
            # Menampilkan pesan keberhasilan pemanggilan jin / summon jin
            print("Mengumpulkan sesajen...")
            print("Menyerahkan sesajen...")
            print("Membacakan mantra...")
            print("Jin",user_name,"berhasil dipanggil!")

            # Menambahkan pasang username, password, dan role jin ke dalam list data_user
            builtin.appendrow_user(user_name, password_input, "jin_pembangun")


