dane = [line.strip() for line in open("strony.txt", 'r')]
brakujące=[] #lista iloscia brakujacych stron z pojedynczych prob
for line in dane:
    kolejka=[]  #kolejka ze stronami
    bufor=[]    #pamiec
    migawki=[]  #migawki kazdego cyklu
    migawka = []    #migawka pojedynczego cyklu
    max=20   #maksymalny rozmiar bufora (pamieci)
    kolejka = line.split(",")
    kolejka.pop()   #usuniecie ostaniej komorki, bo na koncu jest przecinek i jest pustka
    kolejka = list(map(int, kolejka))   #zamiana danych z listy na int
    potrzebny=0 #0 oznacza ze zadna strona nie jest potrzebna
    brakujacy=0 #0 oznacza ze nie ma zadnej brakujacej strony w buforze

    for i in range(len(kolejka)+1):
        if potrzebny!=0:       #czy jakas strona jest w kolejce, jesli nie jest rowny 0 to jest
            if brakujacy!=0:   #jesli brakuje strony w buforze    sprawdz czy jest miejsce
                if len(bufor)<max:    #jesli jest miejsce w buforze
                    bufor.append(kolejka[i-1])  #dodaj strone na koniec
                else:   #jesli nie ma miejsca w buforze
                    bufor.remove(bufor[0])     #usun pierwszy element
                    bufor.append(kolejka[i-1])  #dodaj element na koniec

        #2
        if i < len(kolejka):
            potrzebny=kolejka[i] #sprawdzamy jaka strona bedzie potrzebna po skonczeniu obecnego cyklu
        #3 sprawdzamy czy potrzena strona jest w buforze
        czy_jest = False #zakladamy ze potrzebnej strony nie ma w buforze
        for j in bufor:  # czy jest w buforze
            if potrzebny == j:  # jesli jest to oznacz to
                czy_jest = True
        if czy_jest==True:  #jesli jest w buforze to nie ma brakujacych
            brakujacy=0
        else:   #jesli nie ma w buforze
            if i < len(kolejka):    #sprawdz czy nie skonczyla sie kolejka
                brakujacy=kolejka[i]
        if i == len(kolejka):   #jesli kolejka sie skonczyla ustaw brakujacy na 0 i potrzebny tez
            brakujacy=0
            potrzebny=0

        migawka.append(bufor[:])
        migawka.append(potrzebny)
        migawka.append(brakujacy)
        migawki.append(migawka[:])
        #print(migawka) #mozem zobaczyc kazdy krok dzialania algorytmu
        migawka.clear()

    licznik_brakujacych=0

    for i in migawki:
        if i[2]!=0: #jesli jest jakas brakujaca strona to zlicz to
            licznik_brakujacych+=1

    brakujące.append(licznik_brakujacych) #dodaj do listy z iloscia brakujacych stron w poszczegolnych probach

suma_brakujących=0
for i in brakujące: #zliczanie brakujacych stron
    suma_brakujących += i

wynik=round(suma_brakujących/len(brakujące), 2)
print("srednia ilosc brakujących stron: ", wynik)

with open("FIFO_wyniki.txt", "w") as file:
    file.write("Srednia ilosc brakujacych stron: " + str(wynik))


