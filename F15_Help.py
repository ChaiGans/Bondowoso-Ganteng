import tempat_variable

# Penggunaan nama fungsi helpp() bukan help() diakibatkan "help()" sudah merupakan fungsi bawaan dari python
def helpp(): 
    if (tempat_variable.role_user == "bandung_bondowoso"): 
        print("=======================  HELP  =======================")
        print("1. logout \n   untuk keluar dari akun yang digunakan sekarang")
        print("2. summonjin \n   untuk memanggil jin")
        print("3. hapusjin \n   untuk menghapus jin")
        print("4. ubahjin \n   untuk mengubah tipe jin")
        print("5. batchkumpul \n   untuk memerintahkan jin pengumpul")
        print("6. batchbangun \n   untuk memerintahkan jin pembangun")
        print("7. laporanjin \n   untuk untuk mengetahui kinerja para jin")
        print("8. laporancandi \n   untuk mengetahui progress pembangunan candi")
        print("9. save \n   untuk menyimpan data yang berada di program")
        print("10. exit \n   untuk keluar dari program dan kembali ke terminal")
    elif(tempat_variable.role_user == "roro_jonggrang"): 
        print("=======================  HELP  =======================")
        print("1. logout \n   untuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi \n   untuk menghancurkan candi yang tersedia")
        print("3. ayamberkokok \n   untuk mengakhiri permainan dan menentukan pemenang")
        print("4. save \n   untuk menyimpan data yang berada di program")
        print("5. exit \n   untuk keluar dari program dan kembali ke terminal")
    elif (tempat_variable.role_user == "jin_pengumpul"): 
        print("1. logout \n   untuk keluar dari akun yang digunakan sekarang")
        print("2. kumpul \n   untuk mengumpulkan bahan-bahan yang diperluan untuk membuat candi")
        print("3. save \n   untuk menyimpan data yang berada di program")
        print("4. exit \n   untuk keluar dari program dan kembali ke terminal")
    elif (tempat_variable.role_user == "jin_pembangun"): 
        print("1. logout \n   untuk keluar dari akun yang digunakan sekarang")
        print("2. bangun \n   untuk membangun candi")
        print("3. save \n   untuk menyimpan data yang berada di program")
        print("4. exit \n   untuk keluar dari program dan kembali ke terminal")
    else:
        print("1. login \n   untuk masuk menggunakan akun")
        print("2. exit \n   untuk keluar dari program dan kembali ke terminal")            