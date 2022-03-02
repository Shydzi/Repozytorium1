import math
#
# a = 0x1f
# print('{0:x}'.format(a))
# print(math.pow(math.log(5 + math.pow(math.sin(8), 2)), 1/6))
# x == y
# y != y
# x > y
# x < y
# x >= y
# x <= y

# a = 3
# b = 2
# c = 5
# d = 4
# if a > b:
#     print('liczba', a, 'jest wieksza od liczby',b)
# elif a < b:
#     print('liczba', b, 'jest wieksza od liczby', a)
# else:
#     print('liczba', b, 'jest równa liczbie', a)
#

# if a == b:
#     print('liczby sa rowne')
# else:
#     print('liczby nie sa rowne')
# if (a>b) & (c>d):
#     print(a, 'jest wieksze niz ', b, 'i',c ,'jest wieksze niz',d)
# else:
#     print(a, 'nie jest wieksze niz ', b, 'lub', c, 'nie jest wieksze niz', d)
# print(a)
# print(type(a))
# a = int(a)
# print(a)
# print(type(a))
# a = input('Podaj pierwszą liczbę: ')
# b = input('Podaj drugą liczbę: ')
# c = input('Podaj trzecią liczbę: ')
# d = input('Podaj czwartą liczbę: ')
# a = int(a)
# b = int(b)
# c = int(c)
# d = int(d)
# if (a > b) & (c > d):
#     print(a, 'jest wieksze niz ', b, 'i', c, 'jest wieksze niz', d)
# else:
#     print(a, 'nie jest wieksze niz ', b, 'lub', c, 'nie jest wieksze niz', d)

# for a in range(0, 7, 1):
#     print(a)
# lista = ['cos', 4, 5, 6.5]
# for a in lista:
#     print(a)
# else:
#     print('wyświetlono wszystkie elementy z listy')
# licznik = 0
# while licznik != 11:
#     print(licznik)
#     licznik += 1
# lista = [4, 8, 5, 3, 2, 9,7]
# licznik = 0
# liczba = input('Wpisz liczbę całkowitą: ')
# while licznik != len(lista):
#     if int(liczba) - lista[licznik] == 0:
#         print('liczba ' + str(liczba) + ' - ' + str(lista[licznik])+ ' = 0')
#         break
#     else:
#         licznik += 1
# else:
#     print("żadna z wartości nie dała odpowiedniego wyniku")
# lista = [4, 8, 5, 3, 2, 9, 7]
# lista2 = [5, 6, 9, 2, 4, 7, 3]
# suma = []
# for a in lista:
#     for b in lista2:
#         wynik = a + b
#         suma.append(wynik)
#     print(suma)

# a = input("Podaj pierwszą liczbę: ")
# b = input("Podaj drugą liczbę: ")
# try:
#     a = int(a)
#     b = int(b)
#     wynik = a / b
#     print(wynik)
# except ZeroDivisionError:
#     print("nie można dzielić przez zero")
# except ValueError:
#     print("nie wczytano liczby całkowitej")


#

lista = [1, 5, 9, 7]
słownik = {1:20,'a' : 'b', 'd':29}
# for a in range(0, 15, 1):
#   lista.insert(a, a)
#   lista.extend([a])
# print(lista)
# lista.pop(3)
# lista.remove(1)
# del lista[3]
# lista.sort()
# print(lista)
# słownik.pop('a')
# słownik[1]
słownik.extend([a:b])
print(słownik)