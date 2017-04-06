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

rs = list(np.linspace(0.01, 0.9, 30))  # rate of getting infected
a = 0.5  # rate of recovery
w = 1.0  # rate of realising infection

start_inf = 10
times = 30000
average = 5


def init_duplex():
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
    return society, family

sus = []
inf = []

for r in rs:
    _sus = []
    _inf = []
    for k in xrange(average):
        society, family = init_duplex()
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
        _inf.append(infected)
        _sus.append(N - infected)

    inf.append(np.mean(_inf))
    sus.append(np.mean(_sus))

# plotting
sus_, = plt.plot(rs, sus, color='b')
inf_, = plt.plot(rs, inf, color='r')
plt.xlabel(u'Prawdopodobieństwo zarażenia się')
plt.ylabel(u'Liczba osób')


# control simulation
def init_union():
    g = ig.Graph.union(family, society)
    g.vs()['state'] = 0
    for i in xrange(start_inf):
        node = random.randint(0, N-1)
        g.vs(node)['state'] = 1
    return g

def init_BA():
    _g = ig.Graph.union(family, society)
    m = int(1.0 * len(_g.es()) / N)
    g = ig.Graph.Barabasi(n=N, m=m)
    g.vs()['state'] = 0
    for i in xrange(start_inf):
        node = random.randint(0, N-1)
        g.vs(node)['state'] = 1
    return g

def init_ER():
    _g = ig.Graph.union(family, society)
    g = ig.Graph.Erdos_Renyi(n=N, m=len(_g.es()))
    g.vs()['state'] = 0
    for i in xrange(start_inf):
        node = random.randint(0, N-1)
        g.vs(node)['state'] = 1
    return g

sus = []
inf = []

for r in rs:
    _sus = []
    _inf = []
    for k in xrange(average):
        g = init_ER()
        # g = init_BA()
        for i in xrange(times):
            node = random.randint(0, N-1)
            if g.vs(node)['state'][0] == 1:
                if random.random() < a:
                    g.vs(node)['state'] = 0
            elif sum(g.vs(g.neighbors(node))['state']) > 0:
                if random.random() < r:
                    g.vs(node)['state'] = 1
        infected = sum(g.vs()['state'])
        _inf.append(infected)
        _sus.append(N - infected)

    infected = sum(g.vs()['state'])
    inf.append(np.mean(_inf))
    sus.append(np.mean(_sus))

# plotting
susER, = plt.plot(rs, sus, color='c')
infER, = plt.plot(rs, inf, color='pink')
plt.plot([1.0 / (1.0 + (2.0 * len(g.es()) / N)), 1.0 / (1.0 + (2.0 * len(g.es()) / N))], [0, N], 'k--')
plt.legend([sus_, inf_, susER, infER], [u'zdrowi duplex', u'chorzy duplex', u'zdrowi ER', u'chorzy ER'])
# plt.savefig("plots/duplex3.png")
plt.title("N={}, M={}, av_fam={}, M_ER={}".format(N, M, av_family, len(g.es())))
plt.show()
