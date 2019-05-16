#----Algorytm przydzialu czasu procesora FCFS

#----rozpakowywanie procesow
def rozpakowanie_procesow():
    id = zbior[::3]     #umieszenie id procesow w liscie
    id.pop()  # na koncu linii byl przecinek, trzeba usunac pusta komorke listy
    dzialanie = zbior[1::3]     #umieszenie czasow dzialania procesow w liscie
    przybycie = zbior[2::3]     #umieszenie czasow przybycia procesow w liscie

    #sprawdzenie czy ilosc id, czasow przybycia i czasow dzialania jest rowna
    x = len(id)
    y = len(dzialanie)
    z = len(przybycie)

    if x != y or x != z:
        print("blad pliku")
        exit(1)
    #laczenie danych o procesach w liste i umieszczanie tej listy w liscie z procesami
    for i in range(x):
        proces = []
        proces.append(int(id[i]))
        proces.append(int(dzialanie[i]))
        proces.append(int(przybycie[i]))
        procesy.append(proces)

#----szeregowanie procesow

def szeregowanie_procesow():
    procesy_temp = []   #lista tymczasowa, zbierajaca czasy przybycia procesow
    while True:
        procesy_temp.clear()    #czyszczenie listy z czasami przybycia
        for i in procesy:  # pobieranie danych o czasie przyjscia procesu
            procesy_temp.append(i[2])

        najnizszy_czas = min(procesy_temp)  #znalezienie procesow ktory przyszly najwczesien

        for i in procesy:  # stworzenie listy z nr id z procesow ktore przyszly najwczesniej
            if najnizszy_czas == i[2]:  #jesli znajdziemy proces o najniszym czasie
                kolejka.append(i)       #wstawiamy go do kolejki procesow
                procesy.remove(i)       #usuwamy z listy procesow ktore przyszly
                break                   #rozpoczecie petli while od nowa, zeby 2 procesy nie wykonaly sie w jednym czasie

        if len(procesy) == 0:   #jesli nie bedzie procesow do wykonania to przerwij petle while
            break

#----obliczanie czasow przybycia i cyklu dla procesow z danej proby

def obliczenia():
    czas_pracy=0    #czas pracy programu
    for i in kolejka:   #dla kazdego procesu w kolejce
        if czas_pracy <= i[2]:  #jesli czaa s pracy jest mniejszy od czasu przybycia
            i.append(0)     #ustaw czas oczekiwania procesu na 0
            czas_pracy=i[2] #czas cyklu wynosi tyle ile trwa proces
            i.append(i[1])
            czas_pracy+=i[1]    #dodajemy do czasu pracy, czas ktory zostal poswiecony na wykonanie procesu
        else:
            i.append(czas_pracy-i[2])   #czas oczekiwania wynosi czas pracy minus czas przybycia
            i.append(i[1]+i[3])     #czas cyklu wynosi czas oczekiwania plus czas wykonania
            czas_pracy +=i[1]       #dodajemy do czasu pracy, czas ktory zostal poswiecony na wykonanie procesu

#----obliczanie srenich czasow oczekiwania i cyklu z danej proby

def statystyka():
    suma_oczekiwania = 0    #zmienna na sumowanie czasu oczekiwania dla pojedynczych procesow z proby
    suma_cyklu = 0          #zmienna na sumowanie czasu cyklu dla pojedynczych procesow z proby
    for i in kolejka:       #petla sumujaca dane czasu
        suma_oczekiwania += i[3]
        suma_cyklu += i[4]

    sredni_oczekiwania = round(suma_oczekiwania / len(kolejka), 3)  #obliczanie sredniego czasu oczekiwania z proby
    sredni_cyklu = round(suma_cyklu  / len(kolejka), 3)         #obliczanie sredniego czasu cyklu z proby
    czasy_oczekiwan.append(sredni_oczekiwania)      #umieszacznie w liscie zbierajacych inforacje ze wszystkich prob
    czasy_cykli.append(sredni_cyklu)



#----program glowny
dane = [line.strip() for line in open("procesy.txt", 'r')]      #odczytanie linia po linii danych z pliku
czasy_oczekiwan=[]      #lista ze średnimi czasami oczekiwania z kolejnych prób
czasy_cykli=[]          #lista ze średnimi czasami cyklu z kolejnych prób

for i in dane:          #pętla wykonująca operacje na danych pobranych z pliku tekstowego linia po linii
    zbior = i.split(",")        #dane z linii są rozdzielane po „ , ” i umieszczane w liście „zbior"
    procesy = []        #lista przechowująca przychodzące procesy, które przyszły w pliku (są w kolejności losowej)
    kolejka = []        #lista przechowująca uszeregowane procesy według algorytmu FCFS
    rozpakowanie_procesow()     #funkcja odpowiedzialna za rozpakowanie procesów z pliku
    szeregowanie_procesow()     #funkcja odpowiedzialna za szeregowanie procesów według algorytmu FCFS
    #print(kolejka)             #mozemy wyswietlic poszeregowana liste procesow
    obliczenia()                #funkcja obliczająca czas oczekiwania i czas cyklu dla pojedynczych procesów
    #print(kolejka)             #mozemy wyswielic poszeregowana liste procesow wraz z czasami oczekiwania i cyklu
    statystyka()                #funkcja odpowiedzialna za obliczenie średniego czasu oczekiwania i cyklu z danej próby

suma_1=sum(czasy_oczekiwan)     #suma czasów średniego oczekiwania ze wszystkich prób
suma_2=sum(czasy_cykli)         #suma czasów cykli oczekiwania ze wszystkich prób


oczekiwanie=round(suma_1/len(czasy_oczekiwan),3)
print("Sredni czas oczekiwania w kolejce: ", oczekiwanie, " ms" )
cykl=round(suma_2/len(czasy_cykli),3)
print("Sredni czas cyklu: ", cykl, " ms")

with open("FCFS_wyniki.txt", "w") as file:
    file.write("Sredni czas oczekiwania w kolejce: " + str(oczekiwanie) + " ms")
    file.write('\n')
    file.write("Sredni czas cyklu: " + str(cykl) + " ms")



