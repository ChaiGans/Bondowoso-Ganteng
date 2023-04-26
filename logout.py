import tempat_variable

# Fungsi logout bertujuan untuk keluar dari akun yang sudah di-login
def logout():
    
    # Jika role_user = "-1" maka kondisi program akan dalam keadaan belum login
    tempat_variable.role_user="-1"

    # Menampilkan pesan bahwa logout berhasil
    print("Logout berhasil !")