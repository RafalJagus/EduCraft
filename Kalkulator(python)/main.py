import math


print("MENU\n"
          "1 - Wykonaj zadania z pliku\n"
          "2 - Sam podam wartości\n")
operacjax = input("Co wybierzesz ? ")
if "1" == operacjax:
    PlikDanych = 'dane.txt'
    PlikWynikow = open('wynik.txt', 'w')
    liczba = []
    wynik = []

    with open(PlikDanych) as x:
        line = x.readline()
        cnt = 1
        while line:
            list = line.strip()
            line = x.readline()
            cnt += 1
            liczba.append(list)

    print("Dane wczytane z ", PlikDanych)
    for x in liczba:
        if "-" in x:
            dzialanie = str(int(x[0]) - int(x[2]))
            print(x, "=", dzialanie)
            PlikWynikow.write(x)
            PlikWynikow.write("=")
            PlikWynikow.write(dzialanie)
            PlikWynikow.write("\n")
        elif "+" in x:
            dzialanie = str(int(x[0]) + int(x[2]))
            print(x, "=", dzialanie)
            PlikWynikow.write(x)
            PlikWynikow.write("=")
            PlikWynikow.write(dzialanie)
            PlikWynikow.write("\n")
        elif "*" in x:
            dzialanie = str(int(x[0]) + int(x[2]))
            print(x, "=", dzialanie)
            PlikWynikow.write(x)
            PlikWynikow.write("=")
            PlikWynikow.write(dzialanie)
            PlikWynikow.write("\n")
        elif "^" in x:
            dzialanie = str(int(x[0]) ** int(x[2]))
            print(x, "=", dzialanie)
            PlikWynikow.write(x)
            PlikWynikow.write("=")
            PlikWynikow.write(dzialanie)
            PlikWynikow.write("\n")
        elif "/" in x:
            dzialanie = str(int(x[0]) / int(x[2]))
            print(x, "=", dzialanie)
            PlikWynikow.write(x)
            PlikWynikow.write("=")
            PlikWynikow.write(dzialanie)
            PlikWynikow.write("\n")
        elif "sin" in x:
            dzialanie = str(math.sin(int(x[-2])))
            print(x, "=", dzialanie)
            PlikWynikow.write(x)
            PlikWynikow.write("=")
            PlikWynikow.write(dzialanie)
            PlikWynikow.write("\n")
        elif "cos" in x:
            dzialanie = str(math.cos(int(x[-2])))
            print(x, "=", dzialanie)
            PlikWynikow.write(x)
            PlikWynikow.write("=")
            PlikWynikow.write(dzialanie)
            PlikWynikow.write("\n")
        elif "tan" in x:
            dzialanie = str(math.tan(int(x[-2])))
            print(x, "=", dzialanie)
            PlikWynikow.write(x)
            PlikWynikow.write("=")
            PlikWynikow.write(dzialanie)
            PlikWynikow.write("\n")

    print("Wyniki zapisane  w PlikWynikow.txt")
elif operacjax=="2":
    class Calculator():
        def menu(self):

            print("MENU\n"
                  "1 - dodawanie\n"
                  "2 - odejmowanie\n"
                  "3 - mnożenie\n"
                  "4 - dzielenie\n"
                  "5 - potegowanie\n"
                  "6 - pierwiastkowanie\n"
                  "7 - sinus\n"
                  "8 - cosinus\n"
                  "9 - tangens\n"
                  "10 - Exit\n"
                  "0 - MENU\n")

        def liczba(self):
            while True:
                num = input("Proszę podać liczbe ")
                try:
                    val = int(num)
                except ValueError:
                    print("This is not a number. Please enter a valid number")
                else:
                    return val

        def dodaj(self):
            a = p.liczba()
            b = p.liczba()
            wynik = int(a) + int(b)
            print("wynik dodawania", a, "+", b, "=", wynik)

        def odejmij(self):
            a = p.liczba()
            b = p.liczba()
            wynik = int(a) - int(b)
            print("wynik odejmowania", a, "-", b, "=", wynik)

        def mnozenie(self):
            a = p.liczba()
            b = p.liczba()
            wynik = int(a) * int(b)
            print("wynik mnożenia ", a, "x", b, "=", wynik)

        def dzielenie(self):
            a = p.liczba()
            b = p.liczba()
            wynik = int(a) / int(b)
            print("wynik dzielenia ", a, "/", b, "=", wynik)

        def potegowanie(self):
            a = p.liczba()
            b = p.liczba()
            wynik = a ** b
            print("wynik potęgowania ", a, "^", b, "=", wynik)

        def pierwiastkowanie(self):
            a = p.liczba()
            wynik = math.sqrt(a)
            print("pierwiastek z ", a, "to ", wynik)

        def sinus(self):
            a = p.liczba()
            wynik = math.sin(a)
            print(wynik)

        def cosinus(self):
            a = p.liczba()
            wynik = math.cos(a)
            print(wynik)

        def tangens(self):
            a = p.liczba()
            wynik = math.tan(a)
            print(wynik)


    p = Calculator()
    print(p.menu())

    operacja = input("Co wybierzesz ? ")

    while operacja != "11":
        if operacja == "1":
            print("wybrałeś dodawanie"), p.dodaj()
        elif operacja == "2":
            print("wybrałeś odejmowanie"), p.odejmij()
        elif operacja == "3":
            print("wybrałeś mnożenie"), p.mnozenie()
        elif operacja == "4":
            print("wybrałeś dzielenie"), p.dzielenie()
        elif operacja == "5":
            print("wybrałeś potegowanie"), p.potegowanie()
        elif operacja == "6":
            print("wybrałeś pierwiastkowanie"), p.pierwiastkowanie()
        elif operacja == "7":
            print("Wylicz sinus "), p.sinus()
        elif operacja == "8":
            print("Wylicz cosinus "), p.cosinus()
        elif operacja == "9":
            print("Wylicz tangens  "), p.tangens()
        elif operacja == "0":
            print(p.menu())
        elif operacja == "10":
            break
        else:
            print("Error menu")
        operacja = input("Co wybierzesz ? ")