import numpy as np
import pandas as pd
#====zadanie 2====#
df = pd.read_csv('imiona.csv',header=0, sep=',', decimal='.')
# print(df)
#====zadanie 2.1====#
# print(df[df['Liczba'] > 999])
#====zadanie 2.2====#
# print(df.loc[df['Imie']=='PAWEŁ'])
#====zadanie 2.3====#
# print(df[((df.Rok > 2009) & (df.Rok< 2012))])
#====zadanie 2.4====#
# m = df.loc[df['Plec']=='M']
# k = df.loc[df['Plec']=='K']
# mm = m[['Liczba']]
# mk = k[['Liczba']]
# print(f'Suma dziewcząt:{mk.sum()}\n Suma chłopców:{mm.sum()}\n')
#====zadanie 2.5====#
# m = df.loc[df['Rok']<=2005]
# mk = m[['Liczba']]
# print(mk.sum())
##====zadanie 2.6====#
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
#====zadanie 3.1====#
# m = np.unique(df[['Sprzedawca']])
# m = df.drop_duplicates(['Sprzedawca'])[['Sprzedawca']]
# print(m)
#====zadanie 3.2====#
# m = df['Utarg'].nlargest(n=5)
# print(df.sort_values('Utarg', ascending=False).head())
# print(m)
#====zadanie 3.3====#
# m = df.groupby(['Sprzedawca']).count()
# print(m)
#====zadanie 3.4====#
# m = df.groupby(['Kraj']).count()
# print(m)
#====zadanie 3.5====#
# filter1 = (df['Data zamowienia'] > '2005-01-01') & (df['Data zamowienia'] < '2006-01-01')
# filter2 = df['Kraj']=='Polska'
#
# print(df.loc[filter1 & filter2].count())

# filter1 = (df['Data zamowienia'] > '2004-01-01') & (df['Data zamowienia'] < '2005-01-01')
# print(df.loc[filter1]['Utarg'].mean())
#====zadanie 3.6====#
filter1 = (df['Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] < '2005-01-01')
print(df.loc[filter1])

filter2 = (df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] < '2006-01-01')
print(df.loc[filter2])

df.loc[filter1].to_csv('zamówienia_2004.csv', sep=';', decimal=',')
df.loc[filter2].to_csv('zamówienia_2005.csv', sep=';', decimal=',')
