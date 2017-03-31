#!/usr/bin/python
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import igraph as ig
import numpy as np
import random

# constants
N = 1000
M = 2000
av_family = 3

r = 0.3  # rate of getting infected
a = 1.0  # rate of recovery
w = 1.0  # rate of realising infection

start_inf = 10
times = 100000

# initializations
society = ig.Graph.Erdos_Renyi(n=N, m=M)
family = ig.Graph()

size = 0
while size < N:
    new = np.random.poisson(av_family)
    if new == 0:
        continue
    if N - size < new:
        new = N - size
    family = family.copy() + ig.Graph.Full(new)
    size = len(family.vs())


society.vs()['state'] = 0  # susceptible
family.vs()['state'] = 0  # susceptible
for i in xrange(start_inf):
    node = random.randint(0, N-1)
    society.vs(node)['state'] = 1  # sick
    family.vs(node)['state'] = 1  # sick

sus = []
inf = []

# main loop
for i in xrange(times):
    node = random.randint(0, N-1)

    if society.vs(node)['state'][0] == 1 and family.vs(node)['state'][0] == 1:
        if random.random() < a:
            society.vs(node)['state'] = 0
            family.vs(node)['state'] = 0
        elif random.random() < w:
            society.vs(node)['state'] = 0
    elif society.vs(node)['state'][0] == 0 and family.vs(node)['state'][0] == 1:
        if random.random() < a:
            family.vs(node)['state'] = 0
    elif society.vs(node)['state'][0] == 0 and family.vs(node)['state'][0] == 0:
        society_neigs = society.vs(society.neighbors(node))
        family_neigs = family.vs(family.neighbors(node))
        if sum(society_neigs['state']) + sum(family_neigs['state']) > 0:
            if random.random() < r:
                society.vs(node)['state'] = 1
                family.vs(node)['state'] = 1
    else:
        raise Exception('This shouldn\'t happen')

    infected = sum(family.vs()['state'])
    inf.append(infected)
    sus.append(N - infected)

# plotting
sus_, = plt.plot(range(times), sus, color='b')
inf_, = plt.plot(range(times), inf, color='r')
plt.xlabel(u'Czas')
plt.ylabel(u'Liczba osób')

# control simulation
g = ig.Graph.union(family, society)
g.vs()['state'] = 0
for i in xrange(start_inf):
    node = random.randint(0, N-1)
    g.vs(node)['state'] = 1

sus = []
inf = []

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

# plotting
susER, = plt.plot(range(times), sus, color='c')
infER, = plt.plot(range(times), inf, color='pink')
plt.legend([sus_, inf_, susER, infER], [u'zdrowi duplex', u'chorzy duplex', u'zdrowi ER', u'chorzy ER'])
# plt.savefig("plots/duplex3.png")
plt.show()
