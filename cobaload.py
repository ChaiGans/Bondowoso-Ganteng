from builtin import csvreader
import tempat_variable

def load():
    tempat_variable.data_user=csvreader(tempat_variable.lokasi_file+"\\user.csv")
    tempat_variable.data_candi=csvreader(tempat_variable.lokasi_file+"\\candi.csv")
    tempat_variable.data_bahanbangunan=csvreader(tempat_variable.lokasi_file+"\\bahan_bangunan.csv")