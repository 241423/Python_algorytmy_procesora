dane = [line.strip() for line in open("strony.txt", 'r')]

brakujace=[]

for line in dane:
    strony=[]
    kolejka = []
    bufor = []
    migawki = []
    max = 20  # maksymalny rozmiar bufora
    strony = line.split(",")
    strony.pop()
    strony = list(map(int, strony))
    potrzebny = 0  # 0 oznacza ze zadna strona nie jest potrzebna
    brakujacy = 0  # 0 oznacza ze nie ma zadnej brakujacej strony w buforze


    for i in range(len(strony)):       #numerowanie stron
        kolejka_temp=[]
        kolejka_temp.append(strony[i])
        kolejka_temp.append(i+1)
        kolejka.append(kolejka_temp)

    #print(kolejka) #strony przed dzialaniem algorytmu
    for i in range(len(kolejka)+1):
        if potrzebny!=0:
            if brakujacy!=0:    #jesli jest brakujacy element sprawdz czy jest miejsce w buforze
                if len(bufor)<max:    #jesli jest miejsce w buforze
                    bufor.append(kolejka[i-1])  #dodaj strone na koniec
                else:   #jesli nie ma miejsca
                    kolejnosc_temp=[]
                    for j in bufor: #zapisz w  kolejnosci przyjscia stron z bufora
                        kolejnosc_temp.append(j[1])
                    a=min(kolejnosc_temp)   #znajdz strone ktora przyszla najwczesniej
                    for j in bufor:     #przeszukaj bufor
                        if j[1] == a:   #kiedy znajdziesz najstarsza strone
                            j[0] = kolejka[i-1][0] #zmien numer strony
                            j[1] = kolejka[i - 1][1] #zmien czas przybycia
            else: #jesli nie ma brakujacego elementu
                for j in bufor: #znajdz element ktory jest w buforze i bedze teraz uzywany
                    if j[0]==kolejka[i-1][0]:
                        j[1] = i  #zmien czas uzycia

        if i < len(kolejka):
            potrzebny=kolejka[i] #sprawdzamy co bedzie potrzebne po skonczeniu obecnego cyklu
        #3 sprawdzamy czy potrzena strona jest w buforze
        czy_jest = False  # zakladamy ze potrzebnej strony nie ma w buforze
        for j in bufor:  # czy jest w buforze
            if potrzebny[0] == j[0]:  # jesli jest to oznacz to
                czy_jest = True
        if czy_jest==True:  #jesli jest w buforze to nie ma brakujacych
            brakujacy=0
        else:   #jesli nie ma w buforze
            if i < len(kolejka):    #sprawdz czy nie skonczyla sie kolejka
                brakujacy=kolejka[i]
        if i == len(kolejka):   #jesli kolejka sie skonczyla ustaw brakujacy na 0 i potrzebny tez
            brakujacy=0
            potrzebny=0

        migawka = []
        migawka.append(bufor)
        migawka.append(potrzebny)
        migawka.append(brakujacy)
        migawki.append(migawka)
        #print(migawka) #mozemy sprawdzic dzialanie algorytmu krok po kroku
        #wait=input("kliknij enter")
    #print(migawki)
    licznik_brakujacych=0
    for i in migawki:
        if i[2]!=0:
            licznik_brakujacych+=1

    brakujace.append(licznik_brakujacych)

suma_brakujacych=0
for i in brakujace:
    suma_brakujacych += i
wynik=round(suma_brakujacych/len(brakujace),2)
print("srednia ilosc brakujących stron: ", wynik )
#print(brakujace)
with open("LRU_wyniki.txt", "w") as file:
    file.write("Srednia ilosc brakujacych stron: " + str(wynik))