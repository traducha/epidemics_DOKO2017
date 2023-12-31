#!/usr/bin/python
# -*- coding: utf-8 -*-
import igraph as ig

# deklaracja stałych
N = 50
M = 100
m = int(1.0 * M / N)

# inicjalizacja i rysowanie sieci losowej
g = ig.Graph.Erdos_Renyi(n=N, m=M)
g.vs()['size'] = [i + 10 for i in g.degree()]
layout = ig.Graph.layout_kamada_kawai(g)
ig.plot(g, layout=layout)

# inicjalizacja i rysowanie sieci bezskalowej
g = ig.Graph.Barabasi(n=N, m=m)
g.vs()['size'] = [i + 10 for i in g.degree()]
layout = ig.Graph.layout_kamada_kawai(g)
ig.plot(g, layout=layout)
