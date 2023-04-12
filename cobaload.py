from builtin import csvreader

def load(lokasi,nama):
    nama="\\"+nama+".csv"
    return csvreader(lokasi+nama)