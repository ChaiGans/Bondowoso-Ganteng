import builtin,tempat_variable

# Generate a random integer between 1 and 5
def kumpul():
    pasir_kumpul = builtin.lcg()
    batu_kumpul = builtin.lcg()
    air_kumpul = builtin.lcg()

    print("Jin menemukan",pasir_kumpul, "pasir", batu_kumpul, "batu, dan", air_kumpul, "air.")
    tempat_variable.data_bahanbangunan[1][2] = str(int(tempat_variable.data_bahanbangunan[1][2]) + pasir_kumpul)
    tempat_variable.data_bahanbangunan[2][2] = str(int(tempat_variable.data_bahanbangunan[2][2]) + batu_kumpul)
    tempat_variable.data_bahanbangunan[3][2] = str(int(tempat_variable.data_bahanbangunan[3][2]) + air_kumpul)
