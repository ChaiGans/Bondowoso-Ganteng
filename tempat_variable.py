# Role dan username
role_user=""
nama_user=""

# Lokasi File
lokasi_file=""

# Neff menyatakan banyaknya array yang sudah terisi +1(array index 0 berisi keterangan)
neff_data_user=0
neff_data_candi=0
neff_data_bahanbangunan=0

# Reminder : Data index 0 berisi keterangan 
data_user=[["0" for i in range(3)] for j in range(113)]
data_candi=[["0" for i in range(5)] for j in range(113)]
data_bahanbangunan=[["0"for i in range(3)]for j in range(4)]

# Seed LCG
seed_lcg_pasir = 2
seed_lcg_batu = 10
seed_lcg_air = 6