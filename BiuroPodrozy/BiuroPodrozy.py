import random
from random import randint


wybr_plan = {
    "Miasto": "Nie wybrano zadnego miasta",
    "Liczba dni": 0,
    "Cena": 0,
}
    
wszystkie_oferty = set()

lista_wycieczek = ['Bali', 'Bangkok', 'Dubaj', 'Korfu', 'Kreta', 'Londyn', 'Majorka', 'Malawi', 'Mediolan', 'Nowy Jork', 'Paryż', 'Portoryko', 'Rodos', 'Seul', 'Singapur', 'Tokio']

class Trip:
 wycieczka = ''
 dni = 0
 cena = 0
 def __init__(self, wycieczka, liczbadni, cena):
    self.wycieczka = wycieczka
    self.dni = liczbadni
    self.cena = cena

def funkcja_losowanie(x, y, z):
    while True:
        x = random.choice(lista_wycieczek)
        y = randint(3,30)
        z = randint(2500, 10000)
        print("Oto wygenerowana propozycja:")
        print(x)
        print('Liczba dni: ', end='')
        print(y) 
        print('Cena za osobe: ', end='')
        print(z)
        question = int(input("Czy wymieniona wyzej oferta cie interesuje? \n 1: Tak, powroc do menu \n2: Nie, powroc do menu \n Pozostale cyfry: wylosuj ponownie\n"))
        if question == 1:
            print("wybrano oferte podrozy")
            wybr_plan.update({"Miasto": x})
            wybr_plan.update({"Liczba dni": y})
            wybr_plan.update({"Cena": z})
            wycieczka = Trip(x, y,z)
            wszystkie_oferty.add(wycieczka)
            break
        if question == 2:
            print("Wracamy do menu")
            break
        else:
            print("Losujemy ponownie")

def funkcja_wybor(x, y, z):
    print("Wybierz interesujace cie miasto sposrod listy najchetniej odwiedzanych miejsc: ")
    print(*lista_wycieczek, sep=", ")
    while True:
        x = input("Wpisz nazwe miasta ktora cie interesuje: ")
        if x in lista_wycieczek:
            print("Wybrano miasto")
            y = int(input("Wpisz interesujaca cie dlugosc pobytu od 3 do 30 dni: "))
            if 3 <= y <= 30:
                print("Wybrano ilosc dni")
                z = int(input("Wpisz interesujaca cie cene wycieczki (najtansze zaczynaja sie od 2500): "))
                if z >= 2500:
                    print("Wybrano cene w poprawnym przedziale. Zapisuje wybrana oferte")
                    wybr_plan.update({"Miasto": x})
                    wybr_plan.update({"Liczba dni": y})
                    wybr_plan.update({"Cena": z})
                    wycieczka = Trip(x, y,z)
                    wszystkie_oferty.add(wycieczka)
                    break
                else:
                    print("Zbyt niska cena")
                    break
            else:
                print("Zbyt mala/duza liczba dni")
                break
        else:
            print("Nie ma takiego miasta na liscie")
            break

while True:
    print('Witamy w biurze podrozy. Wybierz opcje, ktora chcesz wykonac: ')
    print('1: Wyszukaj oferte podrozy wedlug swoich preferencji')
    print('2: Wylosuj oferte podrozy')
    print('3: Pokaz wybrane oferty')
    print('4: Pokaz najnowsza wybrana oferte')
    print('0: Wyjdz z biura podrozy')

    wybor = int(input("Wprowadz numer opcji: "))

    match wybor:

        case 1:
            funkcja_wybor(Trip.wycieczka,Trip.dni, Trip.cena)

        case 2:
           wycieczka = ''
           liczbadnirandom = 0
           cenarandom = 0
           funkcja_losowanie(wycieczka, liczbadnirandom, cenarandom)

        case 3:    
            for i in wszystkie_oferty:
                    print("Miasto: ", i.wycieczka)
                    print("Liczba dni: ", i.dni)
                    print("Cena: ", i.cena)
    
        case 4:
            for klucz, wartosc in wybr_plan.items():
                print(klucz, ":", wartosc)
        case 0:
            print('Opuszczasz biuro podrozy. Do zobaczenia.')
            break

        case _:
            print("wpisano nieprawidlowy znak") 