import math
#piatek 15:45-18:00
#30.03 -1 kolokwium
#
# lista=[]
# for element in sekwencja:
#     if warune_na_element:
#         lista.append(akcja_z_elementem)
# lista=[akcja_z_elementem for element in sekwencja if warunek_na_element]
# a = []
# for x in range(0, 10):
#     a.append(x**2)
# print(a)
# a2 = [x**2 for x in range(0, 10)]
# print(a2)
# b = []
# for x in range(0, 6):
#     b.append(3**x)
# print(b)
# b2 = [3**x for x in range(0, 6)]
# print(b2)
# c = []
# for x in a:
#     if(x % 2 == 1):
#         c.append(x)
# print(c)
# c1 = [x for x in a if(x % 2 == 1)]
# print(c1)

# lista = []
# for a in [1, 2, 3]:
#     for b in [4, 5, 6]:
#         lista.append((a,b))
# print(lista)
# lista2 = [(a, b) for a in [1, 2, 3] for b in [4, 5, 6]]
# print(lista2)

# slownik = {'PZU': 'Państwowy zakład ubezpieczeń', 'ZUS': 'Zakład ubezpieczeń społecznych', 'PKO': 'Państwowa kasa oszczędności'}
# slownik_odwrocony = {}
# print(slownik)
# for key, value in slownik.items():
#     slownik_odwrocony[value] = key
# print(slownik_odwrocony)
# #slownik2 = {value: key for value, key in slownik.items()}
# slownik2 = {value: key for key, value in slownik.items()}
# print(slownik2)

# def nazwa_funkcji(argumenty pozycyjne, argumenty domyslne=wartosc,argument z *(dowonla ilosc wartosci np *x),argument z **(wywolanie funkcji z wieloma argumentami z kluczem np **x)):
#     instrukcje
#     return
#     instrukcje(po return zostana pominiete)
# def rownanie_kwadratowe(a, b, c):
#     delta = b**2 - 4 * a * c
#     if delta < 0:
#         return('brak rozwiazan')
#     elif delta == 0:
#         print('jedno roziwiazanie')
#         x = (-b)/(2*a)
#         return x
#     else:
#         print('dwa rozwiazania')
#         x1 = ((-b) - math.sqrt(delta))/(2*a)
#         x2 = ((-b) + math.sqrt(delta))/(2*a)
#         return x1, x2
#
#
# print(rownanie_kwadratowe(6, 1, 3))
# print(rownanie_kwadratowe(1, 2, 1))
# print(rownanie_kwadratowe(1, 4, 1))

# def parzysta(a):
#     if a == 0:
#         return("zero")
#     elif a % 2 == 0:
#         return("parzysta")
#     else:
#         return("Nie parzysta")
# print(parzysta(2))
# print(parzysta(1))
# print(parzysta(0))

# def dlugosc_odcinka(x1=1, y1=2, x2=3, y2=4):
#     return math.sqrt((x2-x1)**2 + (y2-y1)**2)
# #argumenty domyslne
# print(dlugosc_odcinka())
# #artumenty pozycyjne
# print(dlugosc_odcinka(4, 5, 6, 9))
# #dwa arguemnty pozycyjne, dwa okreslone
# print(dlugosc_odcinka(2, 2, y2=7, x2=5))
# #argumenty po za kolejnoscia
# print(dlugosc_odcinka(x2=6, y2=4, x1=2, y1=3))
# #dwa argumenty domyslna wartosc, dwa z nowa wartoscia
# print(dlugosc_odcinka(x2=4, y2=7))

# def ciag(* liczby):
#     if len(liczby) == 0:
#         return 0
#     else:
#         suma = 0
#         for i in liczby:
#             suma += i
#         return suma
# print(ciag())
# print(ciag(1, 2, 3, 4, 5, 6, 7, 8))

# def co_lubie(** rzeczy):
#     for cos in rzeczy:
#         print('to jest')
#         print(cos)
#         print("co lubie")
#         print(rzeczy[cos])
# co_lubie(gry=['planoszowe', 'komputerowe'], slodycze='czekolada')

