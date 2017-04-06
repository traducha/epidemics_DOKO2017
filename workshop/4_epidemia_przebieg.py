#!/usr/bin/python
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import igraph as ig
import random

# deklaracja stałych
N = 1000
M = 2000
m = int(1.0 * M / N)

r = 0.2
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
sus, = plt.plot(range(times), sus, color='b')
inf, = plt.plot(range(times), inf, color='r')
plt.legend([sus, inf], [u'zdrowi', u'chorzy'])
plt.xlabel(u'Czas')
plt.ylabel(u'Liczba osób')
plt.show()
