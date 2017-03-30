#!/usr/bin/python
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import igraph as ig
import random

# deklaracja stałych
N = 1000
M = 2000

r = 0.2
a = 1.0

print('lambda = {}'.format(r/a))
print('wartość krytyczna = {}'.format(N / (2.0 * M)))

start = 100
times = 100000

# inicjalizacja sieci
g = ig.Graph.Erdos_Renyi(n=N, m=M)
g.vs()['state'] = 0  # zdrowy
for i in xrange(start):
    node = random.randint(0, N-1)
    g.vs(node)['state'] = 1  # chory

sus = []
inf = []

# główna pętla symulacji
for i in xrange(times):
    node = random.randint(0, N-1)
    if g.vs(node)['state'][0] == 1:
        if random.random() < a:
            g.vs(node)['state'] = 0
    elif sum(g.vs(g.neighbors(node))['state']) > 0:
        if random.random() < r:
            g.vs(node)['state'] = 1

    infected = sum(g.vs()['state'])
    inf.append(infected)
    sus.append(N - infected)

# tworzenie wykresu
sus, = plt.plot(range(times), sus, color='b')
inf, = plt.plot(range(times), inf, color='r')
plt.legend([sus, inf], [u'zdrowi', u'chorzy'])
plt.xlabel(u'Czas')
plt.ylabel(u'Liczba osób')
plt.show()
