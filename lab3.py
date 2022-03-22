#zad1
# a=[]
# for x in range(1,10):
#     a.append(1-x)
# print(a)
# import math
# b=[]
# for x in range(0,7):
#     b.append(int(math.pow(4,x)))
# print(b)
# c=[]
# for x in b:
#     if x%2==0:
#         c.append(x)
# print(c)
#zad2
# import random
# lista=[]
# for x in range(1,10):
#     lista.append(random.randint(1,99))
# print(lista1)
# lista1=[]
# for x in lista:
#     if x%2==0:
#         lista1.append(x)
# print(lista1)
#zad3
# from itertools import chain
# slownik={'Chleb':'kromki','ziemniaki':'kilogramy','woda':'mililitry','pomidory':'kilogramy','Lody':'sztuki'}
# print(slownik)
# slownik2={}
# for key, value in slownik.items():
#     slownik2.setdefault(value, set()).add(key)
#
# wynik=set(chain.from_iterable(values for key, values in slownik2.items() if len(values)>1))
# print(wynik)
#zad4
# def czyprostokatny(a,b,c):
#     if(a**2+b**2==c**2):
#         print("Trójkąt prostokątny")
#     else:
#         print("Trójkąt nie prostokątny")
#
# a=input("Podaj a: ")
# a=int(a)
# b=input("Podaj b: ")
# b=int(b)
# c=input("Podaj c: ")
# c=int(c)
# czyprostokatny(a,b,c)
#zad5
# def poletrapezu(a=2,b=2,h=2):
#     print("Pole trapezu to: ",((a+b)*h)/2)
#
# poletrapezu()
# a=input("Podaj a: ")
# a=int(a)
# b=input("Podaj b: ")
# b=int(b)
# poletrapezu(a,b)
#zad6
# import math
# def ciag1(a=1,b=4,ile=10):
#     ciag=[]
#     for x in range(0,ile):
#         ciag.append(a*math.pow(b,x))
#     print(ciag)
#     suma=1
#     for y in ciag:
#         suma=suma*y
#     print(suma)
# ciag1()
#zad7
# import math
# def ciag1(*a):
#     ciag=[]
#     for x in range(0,a[2]):
#         ciag.append(a[0]*a[1]**x)
#     print(ciag)
#     suma=1
#     for y in ciag:
#         suma=suma*y
#     print(suma)
# ciag1(1,4,10)
#zad8
# def kasa(**koszyk):
#     suma=0
#     for key,value in koszyk.items():
#         print("Produkt: {} , Cena: {}".format(key,value),"zł")
#     for key,value in koszyk.items():
#         suma=suma+value
#     print("Suma zakupów: ",suma,"zł")
#
# kasa(Jablko= 2, Marchew= 1.5, Bulka= 1.8, Ser= 5, Maka= 5.2, Jajka= 6)
#zad9
from ciagi import *
print(ciagia.an(1,2,3))
print(ciagia.suma(4,5,6))
ciagia.czyary(1,2,3)
ciagia.czyary(1,4,3)
print(ciagia.anzSum(45,43))
print(ciagig.an(1,2,3))
print(ciagig.suma1(43,23))
print(ciagig.ank(12,2,3,1))
print(ciagig.suma0(2,4,5))
ciagig.czygeo(1,2,4)
ciagig.czygeo(1,5,4)