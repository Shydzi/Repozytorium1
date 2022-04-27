import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('imiona.csv',header=0, sep=',', decimal='.')


#====zadanie 1====#
# m = df.groupby("Rok").agg({"Liczba":['sum']})
# print(m)
# m.plot(figsize=(10,6))
# x = 2000
# plt.xticks(range(2000,2017,1))
# plt.show()
#====zadanie 2====#
# p = df.groupby("Plec").agg({"Liczba":['sum']})
# print(p)
# p.plot(kind='bar')
# plt.show()
#====zadanie 3====#
# p = df[df['Rok']==(2012 or 2013 or 2014 or 2015 or 2016 or 2017)].groupby(["Plec"]).agg({"Liczba":['sum']}).value_counts(bins=int)
#
# print(p)
# p.plot(kind='pie',subplots=True)
# plt.show()