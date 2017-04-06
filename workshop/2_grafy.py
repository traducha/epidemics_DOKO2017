#!/usr/bin/python
# -*- coding: utf-8 -*-
import igraph as ig

# deklaracja stałych
N = """WYPEŁNIĆ"""
M = """WYPEŁNIĆ"""
m = 2

# inicjalizacja i rysowanie sieci losowej
g = """INICJALIZACJA SIECI ER"""
g.vs()['size'] = [i + 10 for i in g.degree()]
layout = ig.Graph.layout_kamada_kawai(g)
ig.plot(g, layout=layout)

# inicjalizacja i rysowanie sieci bezskalowej
g = """INICJALIZACJA SIECI BA"""
g.vs()['size'] = [i + 10 for i in g.degree()]
layout = ig.Graph.layout_kamada_kawai(g)
ig.plot(g, layout=layout)
