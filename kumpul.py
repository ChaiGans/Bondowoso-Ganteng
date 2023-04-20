import random,tempat_variable
import builtin

# Generate a random integer between 1 and 5
def kumpul():
    pasir_kumpul = random.randint(1, 5)
    batu_kumpul = random.randint(1, 5)
    air_kumpul = random.randint(1, 5)

    print("Jin menemukan",pasir_kumpul, "pasir", batu_kumpul, "batu, dan", air_kumpul, "air.")
    builtin.data_bahanbangunan[1][2] = str(int(tempat_variable.data_bahanbangunan[1][2]) + pasir_kumpul)
    builtin.data_bahanbangunan[2][2] = str(int(builtin.data_bahanbangunan[2][2]) + batu_kumpul)
    builtin.data_bahanbangunan[3][2] = str(int(builtin.data_bahanbangunan[3][2]) + air_kumpul)

    builtin.cek_current_list()