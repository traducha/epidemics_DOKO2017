#!/usr/bin/python
# -*- coding: utf-8 -*-
import igraph as ig

# deklaracja stałych
N = 50
M = 100
m = 2

# inicjalizacja i rysowanie sieci losowej
g = ig.Graph.Erdos_Renyi(n=N, m=M)
layout = ig.Graph.layout_kamada_kawai(g)
ig.plot(g, layout=layout)

# inicjalizacja i rysowanie sieci bezskalowej
g = ig.Graph.Barabasi(n=N, m=m)
layout = ig.Graph.layout_kamada_kawai(g)
ig.plot(g, layout=layout)
