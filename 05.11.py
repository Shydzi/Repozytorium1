import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
#listing 1
# plt.plot([1, 2, 3, 4])
# plt.ylabel('Jakieś liczby')
# plt.show()
#listing2
# plt.plot([1, 2, 3, 4],[1, 4 ,9 ,16],'ro-')
# plt.axis([0, 6, 0, 20])
# plt.show()
#
# plt.plot([1, 2, 3, 4],[1, 4 ,9 ,16],'r')
# plt.plot([1, 2, 3, 4],[1, 4 ,9 ,16],'o')
#
# plt.axis([0, 6, 0, 20])
# plt.show()

#listing 3
# t = np.arange(0., 5., 0.2)
# plt.plot(t, t, 'r--', t, t**2, 'bs', t**3, 'g^')
# plt.legend(labels=['liniowa', 'kwadratowa', 'szescienna'])
# plt.show()

#listing 4
# x = np.linspace(0, 2, 100)
# plt.plot(x, x, label="liniowa")
# plt.plot(x, x**2, label="kwadratowa")
# plt.plot(x,x**3, label="sześcienna")
#
# plt.xlabel('etykieta x')
# plt.ylabel('etykieta y')
#
# plt.title('Prosty Wykres')
#
# plt.legend()
# plt.savefig('wykres matplot.png')
#
# plt.show()
# im1 = Image.open('wykres matplot.png')
# im1 = im1.convert('RGB')
# im1.save('nowy.jpg')
#listing 5
# x = np.arange(0, 10, 0.1)
# s = np.sin(x)
# plt.plot(x, s, label="sin(x)")
# plt.xlabel('x')
# plt.ylabel('y')
#
# plt.title('Wykres sin(x)')
# plt.legend()
#
# plt.show()
#listing 6
# data = {'a': np.arange((50)),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
# print(f"a={data['a'][0]},b={data['b'][0]}, c={data['c'][0]},d={data['d'][0]}")
# plt.scatter('a', 'b', c='c', s='d', data=data )
# plt.xlabel('wartość a')
# plt.ylabel('wartość b')
# plt.show()
#listing 7
# x1 = np.arange(0, 2, 0.02)
# x2 = np.arange(0, 2, 0.02)
#
# y1 = np.sin(2 * np.pi * x1)
# y2 = np.cos(2 * np.pi * x2)
#
# plt.subplot(2, 1, 1,)
# plt.plot(x1, y1, '-')
# plt.title('wykres sin(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
#
# ax = plt.subplot(2, 1, 2)
# plt.plot(x2, y2, 'r-')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.title('Wykres cos(x)')
# plt.subplots_adjust(hspace=0.5)
# plt.show()
#listing 8
# x1 = np.arange(0, 2, 0.02)
# x2 = np.arange(0, 2, 0.02)
# y1 = np.sin(2 * np.pi * x1)
# y2 = np.cos(2 * np.pi * x2)
#
# fig, axs = plt.subplots(3, 2, )
# axs[0, 0].plot(x1, y1, '-')
# axs[0, 0].set_title('wykres sin(x)')
# axs[0, 0].set_xlabel('x')
# axs[0, 0].set_ylabel('sin(x)')
#
# axs[1, 1].plot(x2, y2, 'r-')
# axs[1, 1].set_title('wykres cos(x)')
# axs[1, 1].set_xlabel('x')
# axs[1, 1].set_ylabel('cos(x)')
#
# axs[2, 0].plot(x2, y2, 'r-')
# axs[2, 0].set_title('wykres cos(x)')
# axs[2, 0].set_xlabel('x')
# axs[2, 0].set_ylabel('cos(x)')
#
# fig.delaxes(axs[0, 1])
# fig.delaxes(axs[1, 0])
# fig.delaxes(axs[2, 1])
# plt.show()
#listing 9

# dane = {'Kraj':['Belgia','Indie','Brazylia','Polska'],
#         'Stolica':['Bruksela',' New Delhi','Brasilia','Warszawa'],
#         'Populacja':[11190846,1303171035,207847528,38675467],
#         'Kontynent':['Europa', 'Azja', 'Ameryka Południowa','Europa']}
# df = pd.DataFrame(dane)
# print(df)
#
# plt.bar(data=df, x='Kontynent', height='Populacja', color=['red', 'green', 'yellow'])
# plt.xlabel('Kontynenty')
# plt.ylabel('Populacja w mld')
# plt.show()
#listing 10
# x = np.random.randn(10000)
# plt.hist(x, bins=50, facecolor='g', alpha=0.75, density=True)
#
# plt.xlabel('Wartości')
# plt.ylabel('Prawdopodobieństwo')
# plt.title('Histogram')
# plt.grid()
# plt.show()
#listing 11
# df = pd.read_csv('dane.csv', header = 0, sep=";", decimal=".")
# print(df)
# seria = df.groupby('Imię i nazwisko')['Wartość zamówienia'].sum()
# wedges, texts, autotext = plt.pie(x=seria, labels=seria.index, autopct=lambda pct:"{:.1f}%".format(pct),textprops=dict(color="black"),colors=['red','green'])
# plt.title('Suma zamówien dla sprzedawców')
# plt.legend(loc='lower right')
# plt.ylabel('Procentowy wynik wartości zamówienia')
# plt.show()