class Film():
    def __init__(self):
        self.tylul = ""
        self.liczba_wypozyczen = 0

    def set_tytul(self, tytul):
        if len(tytul) <= 20:
            self._tytul = tytul
        else:
            print("Tytuł jest za długi, maksymalnie 20 znaków.")

    def get_tylul(self):
        return self.tylul

    def get_liczba_wypozyczen(self):
        return self.liczba_wypozyczen


    def inkrementacja(self):
        self.liczba_wypozyczen += 1

if __name__ == "__main__":
    filmy = Film()
    filmy.set_tytul("Rambo")
    print("Początkowy tytuł filmu:", filmy.get_tylul())
    print("Początkowa liczba wypożyczeń:", filmy.get_liczba_wypozyczen())

    filmy.set_tytul("Incepcja")
    print("Tytuł po ustawieniu:", filmy.get_tylul())

    aktualny_tytul = filmy.get_tylul()
    print("Pobrany tytuł filmu:", aktualny_tytul)

    print("Liczba wypożyczeń przed inkrementacją:", filmy.get_liczba_wypozyczen())
    filmy.inkrementacja()
    print("Liczba wypożyczeń po inkrementacji:", filmy.get_liczba_wypozyczen())
