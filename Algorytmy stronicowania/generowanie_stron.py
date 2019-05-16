import random

x = 100  # liczba prob
y = 100 # liczba procesow w probie

with open("strony.txt", "w") as file:

    for i in range(x):
        for j in range(y):
            a = random.randint(1, 30)
            file.write(str(a) + ",")  # zapis czas dzialania do pliku

        file.write('\n')