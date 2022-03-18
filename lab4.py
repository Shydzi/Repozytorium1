#====zadanie 1====#
# plik=open('zadanie1.txt','w+',encoding='utf-8')
# lista = []
# for x in range(0, 31):
#     lista.append(x*2)
#
# plik.write(str(lista))
# plik.close()
#====zadanie 2====#
# plik = open('zadanie1.txt', 'r')
# wiersze = plik.readlines()
# print(wiersze)
# plik.close()
#====zadanie 3====#
# with open('zadanie1.txt', 'r') as plik:
#     for linia in plik:
#         print(linia, end='')
#====zadanie 4====#
# class NaZakupy():
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produkty = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jed = cena_jed
#     def wyswietl_produkt(self):
#         return self.nazwa_produkty,self.ilosc, self.jednostka_miary, self.cena_jed
#     def ile_produkty(self):
#         return str(self.ilosc) + str(self.jednostka_miary)
#     def ile_kosztuje(self):
#         return self.cena_jed * self.ilosc
#
# cos = NaZakupy('cos',2,'kg',2.99)
# print(cos.wyswietl_produkt())
# print(cos.ile_produkty())
# print(cos.ile_kosztuje())
# nazwa_produkty = 'costam'
#   ilosc =  2
#   jednoskta_miary = 'kg'
#   cena_jed = '2.99'
#   def metoda(self):
#       return "Pierwsza metoda"
#====zadanie 5====#
# class ciagi():
#     def __init__(self,a,n):
#         self.a = a
#         self.n = n
#     def wyswietl_dane(self,a, n):
#         return "a wynosi" +str(a)+" b wynosi "+str(b)
#     def pobierz_elementy(self):
#====zadanie 6====#
# class Robaczek():
#     def __init__(self,x, y ,krok):
#         self.x = x
#         self.y = y
#         self.krok = krok
#     def idz_w_gore(self, ile_krokow):
#         self.y = self.y + ile_krokow * self.krok
#     def idz_w_prawko(self, ile_krokow):
#         self.x = self.x + ile_krokow * self.krok
#     def idz_w_dol(self, ile_krokow):
#         self.y = self.y - ile_krokow * self.krok
#     def idz_w_lewo(self, ile_krokow):
#         self.x = self.x - ile_krokow * self.krok
#     def gdzie_jestem(self):
#         return 'koordynaty x:'+str(self.x)+' y:'+str(self.y)
#
# cos = Robaczek(0,0,10)
# cos.idz_w_gore(2)
# cos.idz_w_prawko(2)
# cos.idz_w_dol(5)
# cos.idz_w_lewo(10)
# print(cos.gdzie_jestem())


