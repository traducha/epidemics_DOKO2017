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

print('lambda = {}'.format(r/a))
print('wartość krytyczna = {}'.format(1.0 / (1.0 + ((2.0 * M) / N))))

start = 100
times = 100000

# inicjalizacja sieci
# g = ig.Graph.Erdos_Renyi(n=N, m=M)
g = ig.Graph.Barabasi(n=N, m=m)
g.vs()['state'] = 0  # zdrowy
for node in random.sample(range(N), start):
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
