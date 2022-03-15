#-----zadanie-1------#
lista=['Piłka nożna','Piłka siatkowa','Boks','Skoki narciarskie','Piłka ręczna']

print(lista)

lista.reverse()

print(lista)

lista.append('Koszykówka')
lista.append('Jazda Konna')

print(lista)

#-----zadanie-2------#
slownik={'M.P.':'Monitor Polski','MSiG':'Monitor Sądowy i Gospodarczy','Dz.Urz.NBP':'Dziennik Urzędowy Narodowego Banku Polskiego'}
print(slownik['M.P.'])

#-----zadanie-3------#
slownikgier={'LOL':'League of Legends','CS:GO':'Counter strike Global Offensive','WOW':'World of Warcraft','WoT':'World of Tanks'}
print(len(slownikgier))

#-----zadanie-4------#
zdanie=input('Podaj zdanie: ')
ile=0
ile=int(ile)
for x in zdanie:
    if x=='a':
        ile+=1
print(ile)

#-----zadanie-5------#
a=input("Podaj a: ")
b=input("Podaj b: ")
c=input("Podaj c: ")
a=int(a)
b=int(b)
c=int(c)
suma=a**b+c
f = open("liczby.txt", "a")
f.write("a^b+c="+str(suma))
f.close()

f = open("liczby.txt", "r")
print(f.readline())

#-----zadanie-6------#
a=input("Podaj a: ")
b=input("Podaj b: ")
c=input("Podaj c: ")
a=int(a)
b=int(b)
c=int(c)
if a>b and a>c:
    print("a jest większe od b i c")
elif b>a and b>c:
    print("b jest większe od a i c")
elif c>a and c>b:
    print("c jest większe od b i a")
else:
    print("a, b i c są równe")

#-----zadanie-7------#
lista1=[2,5,4.6,1,2.7,9,8.9]
for x in lista1:
    print(x**x)

#-----zadanie-8------#
lista2=[]
x=0
while x<10:
    a=input("Podaj liczbe: ")
    a=int(a)
    if a%2==0:
        lista2.append(a)
    x+=1
print(lista2)

#-----zadanie-9------#
import math
x=input("Podaj liczbe: ")
x=int(x)
if x<0:
    print("Liczb ujemnych nie mozna potegowac")
else:
    print(math.sqrt(x))