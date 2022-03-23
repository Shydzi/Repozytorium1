#=====zadanie 1=====#
# class Kształty():
#     #definicja konstruktora
#     def __init__(self, x, y):
#         #deklarujemy atrybuty
#         #self wskazuje ze chodzi o zmienne wlasnie definiowanej klasy
#         self.x = x
#         self.y = y
#         self.opis = "To jest klasa dla ogólnych kształtów"
#
#     def pole(self):
#         return self.x * self.y
#     def obwod(self):
#         return 2 * self.x + 2 * self.y
#     def dodaj_opis(self, text):
#         self.opis = text
#     def skalowanie(self, czynnik):
#         self.x = self.x * czynnik
#         self.y = self.y * czynnik
#
# class Kwadrat(Kształty):
#     def __init__(self, x):
#         self.x = x
#         self.y = x
#
# class KwadratLiteraL(Kwadrat):
#     def obwod(self):
#         return 8 * self.x
#     def pole(self):
#         return 3 * self.x * self.y
#
#
# Kwadrat = Kwadrat(5)
#
# print(Kwadrat.obwod())
# print(Kwadrat.pole())
# Kwadrat.dodaj_opis("Nasza figura to kwadrat")
# print(Kwadrat.opis)
# Kwadrat.skalowanie(0.3)
# print(Kwadrat.obwod())
# print(" ")
#
# litera_l = KwadratLiteraL(5)
# print(litera_l.obwod())
# print(litera_l.pole())
# litera_l.dodaj_opis("litera L")
# print(litera_l.opis)
# litera_l.skalowanie(0.5)
# print(litera_l.obwod())
#=====zadanie 2======#
# class Kwadrat(Kształty):
#     def __init__(self,x):
#         self.x = x
#         self.y = x
#
# kwadrat = Kwadrat(5)
# print(kwadrat)
#
# class Kwadrat(Kształty):
#     def __init__(self, x):
#         self.x = x
#         self.y = x
#
#     def __str__(self):
#         return 'Kwadrat o boku {}'.format(self.x)
#
# kwadrat = Kwadrat(5)
# print(kwadrat)
# class Osoba:
#     def __init__(self, imie, nazwisko):
#         self.imie = imie
#         self.nazwisko = nazwisko
#     def przedstaw_sie(self):
#         return '{} {}'.format(self.imie, self.nazwisko)
#=====zadanie 3======#
# class Pracownik(Osoba):
#     def __init__(self, imie, nazwisko, pensja):
#         #wywołanei konstruktora klasy bazowej
#         Osoba.__init__(self, imie, nazwisko)
#         # lub drugi sposób
#         # super(). __init__(imie, nazwisko)
#         self.pensja = pensja
#     def przedstaw_sie(self):
#         return "{} {} i zarabiam {}".format(self.imie, self.nazwisko ,self.pensja)
#
# class Menedzer(Pracownik):
#     def przedstaw_sie(self):
#         return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)
# jozek = Pracownik('Józef', 'Bajka', 2000)
# adrian = Menedzer('Adrian', 'Mikulski', 12000)
#
# print(jozek.przedstaw_sie())
# print(adrian.przedstaw_sie())
# class Osoba:
#     def __init__(self, imie, nazwisko):
#         self.imie = imie
#         self.nazwisko = nazwisko
#     def przedstaw_sie(self):
#         return '{} {}'.format(self.imie, self.nazwisko)
#
# class Pracownik:
#     def __init__(self, pensja):
#         self.pensja = pensja
#
# class Menedzer(Osoba, Pracownik):
#     def __init__(self, imie, nazwisko, pensja):
#         Osoba.__init__(self, imie, nazwisko)
#         Pracownik.__init__(self, pensja)
#     def przedstaw_sie(self):
#         return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)
#
# adrian = Menedzer('Adrian', 'Mikulski', 12000)
# print(adrian.przedstaw_sie())
#=====zadanie 4======#
# for element in range(1,11):
#     print(element)
#
# imie = "Reks"
# it = iter(imie)
# print(it)
# #na wyjsciu <str_iterator object at 0x00000000027C2640>
# print(next(it))# na wyjsciu R
# print(next(it))# na wyjsciu e
# print(next(it))# na wyjsciu k
# print(next(it))# na wyjsciu s
# print(next(it))# Traceback (most recent call last) :

# class Wspak:
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]
#
# napis = Wspak('Reks')
# print(napis.__next__())
# for a in napis:
#     print(a)
#=====zadanie 5======#
# def reverse(data):
#     for index in range(len(data)-1, -1, -1):
#         yield data[index]
#
# gen = reverse("Feliks")
# print(next(gen))
# print("Marek")
# print(next(gen))
#
# litery = (litera for litera in "łooot?")
# print(litery)
# print(next(litery))
# print(next(litery))
# print(next(litery))
# print(next(litery))
# print(next(litery))
#
