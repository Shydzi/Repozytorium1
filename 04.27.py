import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#
ts = pd.Series(np.random.randn(1000))
ts = ts.cumsum()
#
# ts.plot()
# plt.savefig('wykres.png')
# plt.show()
#
# dane = {'Kraj':['Belgia','Indie','Brazylia','Polska'],
#         'Stolica':['Bruksela',' New Delhi','Brasilia','Warszawa'],
#         'Populacja':[11190846,1303171035,207847528,38675467],
#         'Kontynent':['Europa', 'Azja', 'Ameryka Południowa','Europa']}
# df = pd.DataFrame(dane)
# grupa =df.groupby('Kontynent').agg({'Populacja':['sum']})
#
# grupa.plot(kind='bar',ylabel='Populacja w mld',xlabel='Kontynent', rot=0,legend=True, title='Populacja dla kontynentów',color='turquoise')
# plt.legend(loc='upper left')
# plt.show()

# df = pd.read_csv('dane.csv',header=0, sep=';', decimal='.')
# print(df)
#
# grupa = df.groupby('Imię i nazwisko').agg({'Wartość zamówienia':['sum']})
# print(grupa)
#
# grupa.plot(kind='pie', subplots=True, autopct='%.2f %%',fontsize=20, figsize=(6,6))
# plt.legend(loc='upper left')
# plt.show()

# df = pd.DataFrame(ts)
# print(df)
# df['średnia krocząca'] = df.rolling(window=100).mean()
# print(df)
# df.plot()
# plt.legend(['Wartości', 'Średnia krocząca'])
# plt.show()