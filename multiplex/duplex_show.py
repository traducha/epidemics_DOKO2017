#!/usr/bin/python
# -*- coding: utf-8 -*-
import igraph as ig
import numpy as np
import random
import os

# constants
N = 40
M = 100

r = 0.8  # rate of getting infected
a = 0.5  # rate of recovery
w = 1.0  # rate of realising infection

start_inf = 2
times = 200

# initializations
society = ig.Graph.Erdos_Renyi(n=N, m=M)
family = ig.Graph()

size = 0
while size < N:
    new = np.random.poisson(3)
    if new == 0:
        continue
    if N - size < new:
        new = N - size
    family = family.copy() + ig.Graph.Full(new)
    size = len(family.vs())

layout_both = ig.Graph.layout(society + family)
layout_family = ig.Graph.layout(family)
layout_society = ig.Graph.layout(society)

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

    both = society + family
    for j in xrange(N):
        if society.vs(j)['state'][0] == 0:
            both.vs(j)['color'] = 'green'
        else:
            both.vs(j)['color'] = 'red'
        if family.vs(j)['state'][0] == 0:
            both.vs(N + j)['color'] = 'green'
        else:
            both.vs(N + j)['color'] = 'red'

    # ig.plot(family, layout=layout_family)
    # ig.plot(society, layout=layout_society)
    ig.plot(both, layout=layout_both, target='plots/graph_{}.png'.format(str(i).zfill(3)))

# animation
os.chdir('plots')
os.system('convert -delay 30 -quality 50 graph_*.png animation.gif')
