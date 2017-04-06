#!/usr/bin/python
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import igraph as ig
import random

# deklaracja stałych
N = 1000
M = 2000
m = int(1.0 * M / N)

r = 0.25
a = 1.0

print 'lambda = {}'.format(r/a)
print 'wartość krytyczna = {}'.format(1.0 / (1.0 + ((2.0 * M) / N)))

start = 100
times = 100000

# inicjalizacja sieci
g = """INICJALIZACJA SIECI I NADANIE STANÓW WIERZCHOŁKOM"""

sus = []  # zdrowi
inf = []  # zarażeni

# główna pętla symulacji
for i in xrange(times):
    node = random.randint(0, N-1)
    """WYPEŁNIĆ - ALGORYTM MODELU"""

    infected = sum(g.vs()['state'])
    """ZAPISAĆ LICZBĘ ZARAŻONYCH I ZDROWYCH"""

# tworzenie wykresu
fig = plt.figure()
ax1 = fig.add_subplot('211')
sus, = ax1.plot(range(times), sus, color='b')
ax1.set_ylabel(u'Liczba osób')
ax1.legend([sus], [u'zdrowi'])

ax2 = fig.add_subplot('212')
inf, = ax2.plot(range(times), inf, color='r')
ax2.legend([inf], [u'chorzy'])
ax2.set_xlabel(u'Czas')
ax2.set_ylabel(u'Liczba osób')
plt.show()
