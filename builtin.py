# Builtin function / function yang sering dipake dicopas ke sini biar tinggal dipanggil
import tempat_variable

# Fungsi untuk mencari panjang string "s1"
def lengthstring(s1):
    s1 += "\n"
    cnt = 0
    while(s1[cnt]!='\n'):
        cnt+=1
    return cnt

# Fungsi untuk menambahkan baris user ke dalam list data_user
def appendrow_user(user_name, password, roles):
    list_dummy = [user_name, password, roles]
    tempat_variable.data_user[tempat_variable.neff_data_user]=list_dummy
    tempat_variable.neff_data_user+=1

# Fungsi untuk mengecek apakah nama sudah ada dalam list data_user
def username_checker(username, data):
    count = 0
    for i in range(1,tempat_variable.neff_data_user):
        if data[i][0] == username:
            count += 1
    if count >= 1:
        return False
    elif count < 1:
        return True

# Fungsi untuk mencari pada baris ke berapa "user_name" ditemukan pada data_user
def find_line (data, user_name):
    for i in range (1,tempat_variable.neff_data_user):
        if data[i][0] == user_name:
            return i

# Fungsi yang bertujuan untuk mencari bagian kosong, berguna ketika membangun candi
def carikosong():
    ada=[0 for i in range(103)]
    for i in range(1,tempat_variable.neff_data_candi):
        ada[int(tempat_variable.data_candi[i][0])] = 1
    for i in range(1,103):
        if(ada[i] == 0):
            return i
        
# Fungsi yang bertujuan untuk mengenerasi angka acak dengan algoritma LCG (Linear Congruential Generator)
def lcg():
    x=(tempat_variable.seed_lcg*721+132)%5+1
    tempat_variable.seed_lcg=x
    return x
