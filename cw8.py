import numpy as np
import pandas as pd
#====zadanie 2====#
df = pd.read_csv('imiona.csv',header=0, sep=',', decimal='.')
# print(df)
# print(df[df['Liczba'] > 999])
# print(df.loc[df['Imie']=='PAWEŁ'])
# print(df[((df.Rok > 2009) & (df.Rok< 2012))])
# m = df.loc[df['Plec']=='M']
# k = df.loc[df['Plec']=='K']
# mm = m[['Liczba']]
# mk = k[['Liczba']]
# print(f'Suma dziewcząt:{mk.sum()}\n Suma chłopców:{mm.sum()}\n')

# m = df.loc[df['Rok']<=2005]
# mk = m[['Liczba']]
# print(mk.sum())
#
# liczba = df[['Liczba']]
# print(liczba.sum())

# m = df.loc[df.groupby(["Rok", "Plec"])["Liczba"].idxmax()]
# print(m)
#
# m = df.loc[df.groupby(["Plec"])["Liczba"].idxmax()]
# print(m)
#====zadanie 3====#
df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
print(df)

# m = np.unique(df[['Sprzedawca']])
# m = df.drop_duplicates(['Sprzedawca'])[['Sprzedawca']]
# print(m)

# m = df['Utarg'].nlargest(n=5)
# print(m)

# m = df.groupby(['Sprzedawca']).count()
# print(m)

# m = df.groupby(['Kraj']).count()
# print(m)

# filter1 = (df['Data zamowienia'] > '2005-01-01') & (df['Data zamowienia'] < '2006-01-01')
# filter2 = df['Kraj']=='Polska'
#
# print(df.loc[filter1 & filter2].count())

# filter1 = (df['Data zamowienia'] > '2004-01-01') & (df['Data zamowienia'] < '2005-01-01')
# print(df.loc[filter1]['Utarg'].mean())

filter1 = (df['Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] < '2005-01-01')
print(df.loc[filter1])

filter2 = (df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] < '2006-01-01')
print(df.loc[filter2])

df.loc[filter1].to_csv('zamówienia_2004.csv', sep=';', decimal=',')
df.loc[filter2].to_csv('zamówienia_2005.csv', sep=';', decimal=',')
