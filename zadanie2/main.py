# class Osoba:
#     liczba_instancji = 0
#
#     def __init__(self, id=0, Notatka=""):
#         self.__id = id
#         self.__Notatka = Notatka
#         Osoba.liczba_instancji += 1
#
#     @classmethod
#     def kopiuj(cls, o):
#         return cls(o.__id, o.__imie)
#
#     def przywitaj_sie(self, imie_innej_osoby):
#         if self.__imie:
#             print(f"Notatka : {imie_innej_osoby}{self.__imie}.")
#         else:
#             print("Brak danych")
#
#
# osoba1 = Osoba()
# osoba2 = Osoba(1, "Arturek")
# osoba3 = Osoba.kopiuj(osoba2)
# osoba4 = Osoba(2, 'Adrian')
#
# osoba1.przywitaj_sie("Piotr")
# osoba1.przywitaj_sie("Piotr")
# osoba2.przywitaj_sie("Piotr")
# osoba4.przywitaj_sie("Kasia")
#
# print("Liczba instancji:", Osoba.liczba_instancji)


class Notatka:
    __licznik_notatek = 0

    def __init__(self, tytul, tresc):
        Notatka.__licznik_notatek += 1

        self.__id = Notatka.__licznik_notatek

        self._tytul = tytul
        self._tresc = tresc

    def wyswietl_notatke(self):
        print(f"Tytuł: {self._tytul}")
        print(f"Treść: {self._tresc}")

    def wypisz_dane(self):
        print(f"Notatka: "
              f"{self.__id}; Tytuł: "
              f"{self._tytul}; Treść: "
              f"{self._tresc}")


def main():
    notatka1 = Notatka("Zakupy", "Nic ciekawego")
    notatka2 = Notatka("Spotkanie", "Nic ciekawego")

    print("Notatka :")
    notatka1.wyswietl_notatke()
    print("\nNotatka :")
    notatka2.wyswietl_notatke()

    print("\nDane notatki 1:")
    notatka1.wypisz_dane()
    print("\nDane notatki 2:")
    notatka2.wypisz_dane()


if __name__ == "__main__":
    main()
