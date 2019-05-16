#----Algorytm przydzialu czasu procesora SJF

#----rozpakowywanie procesow
def rozpakowanie_procesow():        #analogicznie jak w fcfs
    id = zbior[::3]
    id.pop()
    dzialanie = zbior[1::3]
    przybycie = zbior[2::3]

    x = len(id)
    y = len(dzialanie)
    z = len(przybycie)

    if x != y or x != z:
        print("blad pliku")
        exit(1)

    for i in range(x):
        proces = []
        proces.append(int(id[i]))
        proces.append(int(dzialanie[i]))
        proces.append(int(przybycie[i]))
        procesy.append(proces)

#----Obliczanie czasu oczekiwania i cyklu procesu
def obliczenia():
    procesy_temp = []   #lista z czasami trwania procesu
    czas_pracy = 0      #zmienna zliczajaca czas pracy wykonywania procesow
    while True:
        for i in procesy:       #dodawanie procesow do kolejki
            if i[2] <= czas_pracy:  #jesli czas przybycia procesu jest nizszy rowny czasu pracy to dodaj do kolejki
                kolejka.append(i)   #dodaje proces do kolejki
                procesy.remove(i)

        if len(kolejka)!=0:     #jesli jest jakis proces w kolejce
            for i in kolejka:  # szukanie procesow ktore trwaja najkrocej
                procesy_temp.append(i[1])

            najnizszy_czas = min(procesy_temp)  #wybranie najnizszego czasy przetwarzania
            procesy_temp.clear()
            for i in kolejka:  # stworzenie listy z nr id z procesow ktore przyszly najwczesniej
                if najnizszy_czas == i[1]:  #jesli znajdzie sie proces z czasem ktory nas interesuje
                    if czas_pracy <= i[2]:  #jesli czas pracy jest mniejszy niz czas przyjscia
                        i.append(0)     #czas oczekiwania jest rowny 0
                        czas_pracy = i[2]   #czas pracy jest rowny czasowi przyjscia procesu
                        i.append(i[1])      #czas cyklu wynosi czas wykonania procesu
                        czas_pracy += i[1]  #czas pracy jest powiekszony o czas wykoniania procesu
                        wyniki.append(i)    #przeniesienie procesu do juz wykonanaych
                        kolejka.remove(i)   #usuniecie procesu z kolejki
                        break               #przerwanie zeby 2 procesy o tym samym czasie przyjscia nie wykonaly sie w tym samym momencie
                    else:       #jezeli czas pracy jest wiekszy niz czas przyjscia
                        i.append(czas_pracy - i[2])     #czas czekania jest rowny czasowi pracy programu minus czasowi przybycia
                        i.append(i[1] + i[3])           #czas cyklu jest rowny czasowi wykonania procesu plus czasowi oczekiwania
                        czas_pracy += i[1]              #czas pracy programu powiekszamy o czas wykoannia procesu
                        wyniki.append(i)                #dodaj proces do juz wykonanych
                        kolejka.remove(i)               #usun proces z kolejki
                        break
            continue #wraca do pierwszego for
        else:
            czas_pracy+=1       #jesli nie ma zadnego procesu w kolejce to zwieksz czas pracy programu
        if len(procesy) == 0:   #jezeli nic nie ma procesach do obliczen to przerwij petle
            break

#----obliczenie sredniego czasu oczekiwania i cyklu z proby
def statystyka():
    suma_oczekiwania = 0
    suma_cyklu = 0
    for i in wyniki:
        suma_oczekiwania += i[3]
        suma_cyklu += i[4]

    sredni_oczekiwania = round(suma_oczekiwania / len(wyniki), 3)
    sredni_cyklu = round(suma_cyklu / len(wyniki),3)
    czasy_oczekiwan.append(sredni_oczekiwania)
    czasy_cykli.append(sredni_cyklu)

#----glowny program
dane = [line.strip() for line in open("procesy.txt", 'r')]
czasy_oczekiwan=[]      #lista ze średnimi czasami oczekiwania z kolejnych prób
czasy_cykli=[]          #lista ze średnimi czasami cyklu z kolejnych prób
for i in dane:
    procesy = []
    kolejka = []
    wyniki=[]
    zbior = i.split(",")
    rozpakowanie_procesow()
    obliczenia()
    #print(wyniki) #mozna zobaczyc posortowane procesy wraz z czasami oczekiwania i cyklu
    statystyka()


suma_1=sum(czasy_oczekiwan)     #suma czasów średniego oczekiwania ze wszystkich prób
suma_2=sum(czasy_cykli)         #suma czasów cykli oczekiwania ze wszystkich prób

oczekiwanie=round(suma_1/len(czasy_oczekiwan),3)
print("Sredni czas oczekiwania w kolejce: ", oczekiwanie, " ms" )
cykl=round(suma_2/len(czasy_cykli),3)
print("Sredni czas cyklu: ", cykl, " ms")

with open("SJF_wyniki.txt", "w") as file:
    file.write("Sredni czas oczekiwania w kolejce: " + str(oczekiwanie) + " ms")
    file.write('\n')
    file.write("Sredni czas cyklu: " + str(cykl) + " ms")

