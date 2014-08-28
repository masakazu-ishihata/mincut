#! /usr/bin/env python

################################################################################
# Import
################################################################################
from numpy import *

################################################################################
# for util
################################################################################
def falses(n):
    return array( [False for i in xrange(n)] )

def trues(n):
    return array( [True for i in xrange(n)] )

################################################################################
# Edmonds-Karp algorithm
################################################################################

########################################
# find an s-t max flow
########################################
def stmaxflow(s, t, C):
    n = len(C)                      # # of nodes
    f = 0                           # current max flow
    F = zeros( [n, n], dtype=float) # current flow matrix

    while 1:
        # search a shortest augmenting path
        m, P = __ShortestAugmentingPath(s, t, C, F)

        # no more flow
        if m == 0: break

        # add flow
        f += m
        v = t
        while v != s:
            u = P[v]
            F[u, v] = F[u, v] + m
            F[v, u] = F[v, u] - m
            v = u

    return f, F

########################################
# find a shortest augmenting path from the current flow network
########################################
def __ShortestAugmentingPath(s, t, C, F):
    # initialize
    P = array([-1     for i in xrange(len(C))]) # parent list (path)
    M = array([sum(C) for i in xrange(len(C))]) # current max flow

    # check as start
    P[s] = -2

    # search list
    q = list([s])
    while len(q) > 0:
        u = q.pop(0)
        # u -> v s.t. unvisited and leeway
        for v in arange(len(C))[logical_and(P == -1, C[u] - F[u] > 0)]:
            P[v] = u                             # visited from u
            M[v] = min(M[u], C[u, v] - F[u, v])  # current flow
            if v == t: return M[t], P            # reach terminal
            q.append(v)

    return 0, P

########################################
# find an s-t min cut
########################################
def stmincut(s, t, C):
    # max flow
    n = len(C)
    f, F = stmaxflow(s, t, C)

    # cutset c
    c = ones(n) # reachability
    c[s] = 0    # s is in 0 side
    q = list([s])
    while len(q) > 0:
        u = q.pop(0)
        for v in arange(n)[ C[u] - F[u] > 0 ]:
            if c[v] == 1:
                c[v] = 0
                q.append(v)

    return f, c

########################################
# find an min cut
########################################
def mincut(C):
    min_f = sum(C)
    min_i = 0
    min_j = 0

    # test each node pair
    for i in xrange(len(C)-1):
        for j in xrange(i+1, len(C)):
            f, c = stmincut(i, j, C)
            if f < min_f:
                min_i = i
                min_j = j
                min_f = f

    return stmincut(min_i, min_j, C)

########################################
# find k min cut
########################################
def kmincut(C, k):
    n  = len(C) # # nodes
    mf = sum(C) # maximum flow (!= max flow)

    # final result
    tf = 0
    tc = zeros(n)

    # initialize
    ms = [ [] for l in xrange(k) ] # ms[l] = members of l-th group
    fs = [ mf for l in xrange(k) ] # fs[l] = maxflow if cut l-th group
    cs = [ [] for l in xrange(k) ] # cs[l] = cut set if cut l-th group

    # first cut
    ms[0] = trues(n)
    fs[0], cs[0] = mincut(C)

    # search
    for l in xrange(1, k):
        # choose the cutting group
        i = argmin(fs)

        # add maxflow
        tf += fs[i]

        # update ms
        m = ms[i]
        c = cs[i]
        v = arange(n)[m] # members of i-th group

        ms[i] = falses(n)
        ms[l] = falses(n)
        for j in v[c == 0]: ms[i][j] = True
        for j in v[c == 1]: ms[l][j] = True

        # update fs & cs
        for j in [i, l]:
            m = ms[j]
            C0 = C[m, :][:, m]
            f0, c0 = mincut(C0)
            fs[j] = f0 if len(c0) > 1 else mf
            cs[j] = c0

    # cutset
    v = arange(n)
    for i in xrange(1, k):
        m = ms[i]
        for j in v[m]:
            tc[j] = i

    return tf, tc
