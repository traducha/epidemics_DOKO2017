#!/usr/bin/python
# -*- coding: utf-8 -*-
import igraph as ig
import random
import os

# deklaracja stałych
N = 30
M = 80

r = 1.0
a = 1.0

start = 10
times = 200

# inicjalizacja sieci
g = ig.Graph.Erdos_Renyi(n=N, m=M)
g.vs()['state'] = 0  # zdrowy
g.vs()['color'] = 'green'
for node in random.sample(range(N), start):
    g.vs(node)['state'] = 1  # chory
    g.vs(node)['color'] = 'red'

# zapisanie układu sieci
g.vs()['size'] = [i + 10 for i in g.degree()]
layout = ig.Graph.layout_kamada_kawai(g)
ig.plot(g, layout=layout)

# czyszczenie katalogu do zapisau obrazków
os.system('rm plots/plot_*')

# główna pętla symulacji
for i in xrange(times):
    node = random.randint(0, N-1)
    if g.vs(node)['state'][0] == 1:
        if random.random() < a:
            g.vs(node)['state'] = 0
            g.vs(node)['color'] = 'green'
    elif sum(g.vs(g.neighbors(node))['state']) > 0:
        if random.random() < r:
            g.vs(node)['state'] = 1
            g.vs(node)['color'] = 'red'

    ig.plot(g, layout=layout, target='plots/plot_{}.png'.format(str(i).zfill(3)))

# tworzenie animacji i wykresu
os.chdir('plots')
os.system('convert -delay 30 -quality 50 plot_*.png animation.gif')
