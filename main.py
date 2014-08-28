#! /usr/bin/env python

from numpy import *
from scipy import stats
from random import *
from mincut import *
import sys

################################################################################
# main
################################################################################
# load # nodes
n = int( raw_input() )

# load edges
C = zeros([n, n])
for line in sys.stdin:
    u, v, c = map(lambda x : int(x),  line.split())
    C[u][v] = c

# mincut
f, c = mincut(C)
v = arange(n)
print f
print v[c == 0]
print v[c == 1]
