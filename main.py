from login import login
from logout import logout

user_input = str(input())  
if user_input == "login":
    x = login()
    while (x == False): # Jika login tidak berhasil, maka meminta inputan user lagi
        user_input = str(input())
    if user_input == "login":
        help()
    else:
        while (user_input != "logout"):
            user_input = str(input())
        logout()