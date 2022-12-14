# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veriler = pd.read_csv("dolar_veri.csv")
print(veriler)

x = veriler.iloc[:,0:1] #gunler
y = veriler.iloc[:, 1:2] #veriler
"""
print(x)
print(y)
print(type(x))
"""
print(x.shape)
dolar_list = list(x.shape)
gun_veri = dolar_list[0] + 1
print(gun_veri)

X = x.values
Y = y.values

print(X)
print(Y)

print(type(X))

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,Y)
plt.plot(X,Y,color="red")
plt.plot(x,lin_reg.predict(X),color="blue")
plt.title("Son {} Gün Dolar Grafiği".format(gun_veri))
plt.xlabel("Günler")
plt.ylabel("Değerler")
plt.show()

#27 temmuzda itibaren alınan Google verileri kullanıştır. Bugünü 26 agustos olarak esas alınız. Bulunduğunuz gunden itibaren kaç gün sonrasını tahmin etmek için sayı giriniz.
# 26 ağustostan sonraki günleri verisi tahmin edilecektir.
print("Gun Yazınız: ")
gun = int(input())

degerList = []

#print(lin_reg.predict([[23]]))
for i in range(gun):
  print("Önünüzdeki ",i+1,".gün tahmini")
  print(lin_reg.predict([[i+gun]]))
  sayi = lin_reg.predict([[i+gun]])
  degerList.append(sayi)

degerlist2 = []
for i in range(gun):
  b = float(degerList[i])
  degerlist2.append(b)
print(degerlist2)

ls_gun = []
for i in range(gun):
  ls_gun.append(i+1)
print(ls_gun)

isim = ['gun']
veriseti = pd.DataFrame(data=ls_gun, columns=isim)
print(veriseti)

isim2 = ['deger']
veriseti2 = pd.DataFrame(data=degerlist2, columns=isim2)
print(veriseti2)

x_gun = veriseti.iloc[:,0:1]
y_deger = veriseti2.iloc[:,0:1]

A = x_gun.values
B = y_deger.values

print(A)
print(B)

from sklearn.linear_model import LinearRegression
lin_reg2 = LinearRegression()
lin_reg2.fit(A,B)
plt.plot(A,B,color="red")
#plt.plot(x_gun,lin_reg2.predict(A),color="blue")
plt.title("Gelecek {} Gün Dolar Grafiği".format(gun))
plt.xlabel("Günler")
plt.ylabel("Değerler")
plt.show()
