import random
from builtin import csvreader, length, appendrow_candi, update_csv

# Generate a random integer between 1 and 5
pasir_kumpul = random.randint(1, 5)
batu_kumpul = random.randint(1, 5)
air_kumpul = random.randint(1, 5)

data = csvreader ('bahan_bangunan.csv')

print("Jin menemukan",pasir_kumpul, "pasir", batu_kumpul, "batu, dan", air_kumpul, "air.")
update_csv('bahan_bangunan.csv', 1, 2, int(data[1][2]) + pasir_kumpul)
update_csv('bahan_bangunan.csv', 2, 2, int(data[2][2]) + batu_kumpul)
update_csv('bahan_bangunan.csv', 3, 2, int(data[3][2]) + air_kumpul)