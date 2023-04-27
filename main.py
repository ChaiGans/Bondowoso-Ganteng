import argparse, time, os, tempat_variable
from login import login
from logout import logout
from summonjin import summonjin
from hapusjin import hapusjin
from ubahjin import ubahjin
from bangun import bangun
from kumpul import kumpul
from batchbangun import batchbangun
from batchkumpul import batchkumpul
from laporanjin import laporanjin
from laporancandi import laporancandi
from F11_hancurkancandi import hancurkancandi
from F12_ayemberkokok import ayamberkokok
from cobaload import load
from cobasave import save
from F15_Help import helpp
from f16_exit import keluar

parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", default ="",nargs="?")
args = parser.parse_args()

if args.nama_folder=="":
    print("Tidak ada nama folder yang diberikan!")
    print()
    print("Usage: python main.py <nama_folder>")
    exit()

folderload=args.nama_folder
args.nama_folder="save\\"+args.nama_folder

if os.path.isdir("save")==False:
    print('Folder parent "save" tidak ditemukan.')
    exit()

if os.path.isdir(args.nama_folder)==False:
    print('Folder "'+folderload+'" tidak ditemukan.')
    exit()

# pengambilan seed lcg awal dari waktu
current_time = time.time()
local_time = time.localtime(current_time)
tempat_variable.seed_lcg = int(local_time.tm_sec)

print("Loading...")
tempat_variable.lokasi_file=str(args.nama_folder)
load()
#print(tempat_variable.data_user)
#print(tempat_variable.data_candi)
#print(tempat_variable.data_bahanbangunan)
print('Selamat datang di program “Manajerial Candi”')
print("Silahkan masukkan username Anda")

tempat_variable.role_user = "-1"
inp=input(">>> ")
count = 0
while(True):
    if(inp=="login"):
        if(not tempat_variable.role_user!="-1"):
            current_username = login()
        else:
            print("Login gagal!")
            print("Anda telah login dengan username", current_username , "silahkan lakukan “logout” sebelum melakukan login kembali.")
    elif(inp=="logout"):
        if(not tempat_variable.role_user!="-1"):
            print("Logout gagal!")
            print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        else:
            logout()
    elif(inp=="summonjin"):
        if(tempat_variable.role_user!="-1" and tempat_variable.role_user=="bandung_bondowoso"):
            summonjin()
        elif(not tempat_variable.role_user!="-1"):
            print("Summon Jin gagal!")
            print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan Summon Jin")
        elif(tempat_variable.role_user!="bandung_bondowoso"):
            print('Summon jin hanya dapat diakses oleh Bandung Bondowoso. Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
    elif(inp=="hapusjin"):
        if(tempat_variable.role_user!="-1" and tempat_variable.role_user=="bandung_bondowoso"):
            hapusjin()
        elif(not tempat_variable.role_user!="-1"):
            print("Hilangkan Jin gagal!")
            print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan Hilangkan Jin")
        elif(tempat_variable.role_user!="bandung_bondowoso"):
            print('Hapus jin hanya dapat diakses oleh Bandung Bondowoso. Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
    elif(inp=="ubahjin"):
        if(tempat_variable.role_user!="-1" and tempat_variable.role_user=="bandung_bondowoso"):
            ubahjin()
        elif(not tempat_variable.role_user!="-1"):
            print("Ubah Tipe Jin gagal!")
            print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan Ubah Tipe Jin")
        elif(tempat_variable.role_user!="bandung_bondowoso"):
            print('Ubah jin hanya dapat diakses oleh Bandung Bondowoso. Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
    elif(inp=="bangun"):
        if(tempat_variable.role_user!="-1" and tempat_variable.role_user=="jin_pembangun"):
            bangun()
        elif(not tempat_variable.role_user!="-1"):
            print("Jin Pembangun gagal!")
            print("Anda belum login, silahkan login terlebih dahulu sebelum memanggil fungsi Jin Pembangun")
        elif(tempat_variable.role_user!="jin_pembangun"):
            print('Bangun hanya dapat diakses oleh Jin Pembangun. Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
    elif(inp=="kumpul"):
        if(tempat_variable.role_user!="-1" and tempat_variable.role_user=="jin_pengumpul"):
            kumpul()
        elif(not tempat_variable.role_user!="-1"):
            print("Jin Pengumpul gagal!")
            print("Anda belum login, silahkan login terlebih dahulu sebelum memanggil fungsi Jin Pengumpul")
        elif(tempat_variable.role_user!="jin_pengumpul"):
            print('Kumpul hanya dapat diakses oleh Jin Pengumpul. Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
    elif(inp=="batchkumpul"):
        if(tempat_variable.role_user!="-1" and tempat_variable.role_user=="bandung_bondowoso"):
            batchkumpul()
        elif(not tempat_variable.role_user!="-1"):
            print("Batch Kumpul gagal!")
            print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan Batch Kumpul")
        elif(tempat_variable.role_user!="bandung_bondowoso"):
            print('Batchkumpul hanya dapat diakses oleh Bandung Bondowoso. Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
    elif(inp=="batchbangun"):
        if(tempat_variable.role_user!="-1" and tempat_variable.role_user=="bandung_bondowoso"):
            batchbangun()
        elif(not tempat_variable.role_user!="-1"):
            print("Batch Bangun gagal!")
            print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan Batch Bangun")
        elif(tempat_variable.role_user!="bandung_bondowoso"):
            print('Batchbangun hanya dapat diakses oleh Bandung Bondowoso. Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
    elif(inp=="laporanjin"):
        if(tempat_variable.role_user!="-1" and tempat_variable.role_user=="bandung_bondowoso"):
            laporanjin()
        elif(not tempat_variable.role_user!="-1"):
            print("Ambil Laporan Jin gagal!")
            print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan Ambil Laporan Jin")
        elif(tempat_variable.role_user!="bandung_bondowoso"):
            print('Laporan Jin hanya dapat diakses oleh Bandung Bondowoso. Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
    elif(inp=="laporancandi"):
        if(tempat_variable.role_user!="-1" and tempat_variable.role_user=="bandung_bondowoso"):
            laporancandi()
        elif(not tempat_variable.role_user!="-1"):
            print("Ambil Laporan Candi gagal!")
            print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan Ambil Laporan Candi")
        elif(tempat_variable.role_user!="bandung_bondowoso"):
            print('Laporan Candi hanya dapat diakses oleh Bandung Bondowoso. Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
    elif(inp=="hancurkancandi"):
        if(tempat_variable.role_user!="-1" and tempat_variable.role_user=="roro_jonggrang"):
            hancurkancandi()
        elif(not tempat_variable.role_user!="-1"):
            print("Hancurkan Candi gagal!")
            print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan Hancurkan Candi")
        elif(tempat_variable.role_user!="roro_jonggrang"):
            print('Hancurkan Candi hanya dapat diakses oleh Roro Jonggrang. Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
    elif(inp=="ayamberkokok"):
        if(tempat_variable.role_user!="-1" and tempat_variable.role_user=="roro_jonggrang"):
            ayamberkokok()
        elif(not tempat_variable.role_user!="-1"):
            print("Ayam Berkokok gagal!")
            print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan Ayam Berkokok")
        elif(tempat_variable.role_user!="roro_jonggrang"):
            print('Ayam Berkokok hanya dapat diakses oleh Roro Jonggrang. Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
    elif(inp=="save"): 
        if(tempat_variable.role_user!="-1"):
            save()
        elif(not tempat_variable.role_user!="-1"):
            print("Save gagal!")
            print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan Save")
    elif(inp=="exit"):
        keluar()
        exit()
    elif(inp=="help"): helpp()
    else:
        if count == 0 :
            helpp()
        else:
            print('Command',inp,'tidak tersedia.','Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
        count+=1
    inp=input(">>> ")

