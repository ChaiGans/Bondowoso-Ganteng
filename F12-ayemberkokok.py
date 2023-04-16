from builtin import length, csvreader

data_candi = csvreader('candi.csv')

def ayamberkokok():    
    print("Kukuruyuk..Kukuruyuk")

    if (length(data_candi)< 100): 
        print("Jumlah Candi:", str(length(data_candi)))
        print("Selamat, Roro Jonggrang Memenangkan Permainan")
        print("")
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
    else: 
        print("Jumlah Candi:", str(length(data_candi)))
        print("Yah, Bandung Bondowoso Memenangkan Permainan!")
    