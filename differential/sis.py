#!/usr/bin/python
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt

# deklaracja stałych
N = 1000.0
I_0 = 1.0

a = 1.0
r = 0.004

times = 5000
dt = 0.001

# inicjalizacja zmiennych
I = [I_0]
S = [N - I_0]
T = [0]

# główna pętla
for i in range(1, times):
    I.append(I[i-1] + (r * (N - I[i-1]) * I[i-1] - a * I[i-1]) * dt)
    S.append(N - I[i])
    T.append(T[i-1] + dt)

# rysowanie wykresu
sus, = plt.plot(T, S, color='b')
inf, = plt.plot(T, I, color='r')
plt.plot([0, times*dt], [a/r, a/r], 'k--')
plt.legend([sus, inf], [u'zdrowi', u'chorzy'])
plt.xlabel(u'Czas')
plt.ylabel(u'Liczba osób')
plt.show()
