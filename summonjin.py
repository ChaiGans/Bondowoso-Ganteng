import csv
from builtin import length
from builtin import appendrow_user

with open("./user.csv", 'r') as file:
#https://earthly.dev/blog/csv-python/
    csvreader = csv.reader(file, delimiter = ";")
    data = [row for row in csvreader]

def cek_username (user_name):
    count = 0
    for i in range (length(data)):
        if data[i][0] == user_name:
            count+=1
    if count>=1: # False jika sudah pernah ada
        return False
    else:   # True jika tidak ada
        return True

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
    while not cek_username (user_name):
        print('Username "'+str(user_name)+'" sudah diambil!')
        print("Masukkan username jin: ", end="")
        user_name = str(input())

    print("Masukkan password jin: ", end ="")
    password_input = str(input())
    while length(password_input) < 5 or length(password_input) > 25:
        print("Password panjangnya harus 5-25 karakter!")
        print("Masukkan password jin: ", end ="")
        password_input = str(input())
    
    print("Mengumpulkan sesajen...")
    print("Menyerahkan sesajen...")
    print("Membacakan mantra...")
    print("Jin",user_name,"berhasil dipanggil!")

    appendrow_user(user_name, password_input, "jin_pengumpul")
    
elif jenis_jin == 2:
    print('Memilih jin "Pembangun"')
    print("Masukkan username jin: ", end="")
    user_name = str(input())
    while not cek_username (user_name):
        print('Username "'+str(user_name)+'" sudah diambil!')
        print("Masukkan username jin: ", end="")
        user_name = str(input())

    print("Masukkan password jin: ", end ="")
    password_input = str(input())
    while length(password_input) < 5 or length(password_input) > 25:
        print("Password panjangnya harus 5-25 karakter!")
        print("Masukkan password jin: ", end ="")
        password_input = str(input())
    
    print("Mengumpulkan sesajen...")
    print("Menyerahkan sesajen...")
    print("Membacakan mantra...")
    print("Jin",user_name,"berhasil dipanggil!")

    appendrow_user(user_name, password_input, "jin_pembangun")

    

