#role dan username
role_user=""
nama_user=""

# lokasi file
lokasi_file=""

#neff menyatakan banyak array yg sudah terisi +1(array index 0 berisi keterangan)
neff_data_user=0
neff_data_candi=0
neff_data_bahanbangunan=0

#data index 0 berisi keterangan 
data_user=[["0" for i in range(3)] for j in range(113)]
data_candi=[["0" for i in range(5)] for j in range(113)]
data_bahanbangunan=[["0"for i in range(3)]for j in range(4)]

#seed lcg
seed_lcg=0