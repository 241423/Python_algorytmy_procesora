# -----biblioteki
import random

x = 100  # liczba prob
y = 100 # liczba procesow w probie

with open("procesy.txt", "w") as file:

    for i in range(x):
        for j in range(y):
            file.write(str(j) + ",") #zapis id do pliku

            a = random.randint(1, 20)   #wylosuj liczbe od 1 do 20
            file.write(str(a) + ",")  # zapis czas dzialania do pliku

            b = random.randint(0, 20)   #wylosuj liczbe od 0 do 20
            file.write(str(b) + ",")  # zapis czas przybycia do pliku

        file.write('\n') #na koncu przejdz do nastepnej linii