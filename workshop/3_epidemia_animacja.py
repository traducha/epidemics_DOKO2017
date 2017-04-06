#!/usr/bin/python
# -*- coding: utf-8 -*-
import igraph as ig
import random
import os

# deklaracja stałych
N = 30
M = 80

r = 1.0  # prawdopodobieństwo zarażenia się
a = 1.0  # prawdopodobieństwo wyzdrowienia

start = 10
times = 200

# inicjalizacja sieci
g = """INICJALIZACJA SIECI"""
g.vs()['state'] = 0  # zdrowy
g.vs()['color'] = """KOLOR ZDROWEGO"""
for i in xrange(start):
    node = random.randint(0, N-1)
    g.vs(node)['state'] = 1  # chory
    g.vs(node)['color'] = """KOLOR CHOREGO"""

# zapisanie układu sieci
g.vs()['size'] = [i + 10 for i in g.degree()]
layout = """WYPEŁNIĆ"""
ig.plot(g, layout=layout)

# czyszczenie katalogu do zapisau obrazków
os.system('rm plots/plot_*')

# główna pętla symulacji
for i in xrange(times):
    node = random.randint(0, N-1)
    """WYPEŁNIĆ - ALGORYTM MODELU"""

    ig.plot(g, layout=layout, target='plots/plot_{}.png'.format(str(i).zfill(3)))

# tworzenie animacji i wykresu
os.chdir('plots')
os.system('convert -delay 30 -quality 50 plot_*.png animation.gif')
