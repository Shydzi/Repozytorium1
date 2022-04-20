import numpy as np
import pandas as pd
#====zadanie 1====#
df = pd.read_csv('imiona.csv',header=0, sep=',', decimal='.')
# print(df)
# print(df[df['Liczba'] > 999])
# print(df.loc[df['Imie']=='PAWEŁ'])
# print(df[((df.Rok > 2009) & (df.Rok< 2012))])
licznik = 0
for x in df[((df['Rok'] > 1999) & (df['Rok'] < 2006))]:
    print(x)
print(licznik)