from network import network
from catcher import catcher
from deck import deck
from dealer import dealer
from game import game
from basicAlpha import basicAlpha
from basicBeta import basicBeta
from basicDelta import basicDelta
from basicEpsilon import basicEpsilon
from HiLo import HiLo
from HiOpt1 import HiOpt1
from HiOpt2 import HiOpt2
from KO import KO
from Halves import Halves
from Omega2 import Omega2
from Red7 import Red7
from Zen import Zen


netDict = {
        'lr': .05,
        'inputs': ['count', 'hand', 'dealerUp'],
        'hidden': [50, 50, 25, 10, 5],
        'outputs': ['hit', 'stay']
        }

#initialize a bunch of players
d = dealer()
d1 = dealer()
ba = basicAlpha()
ba1 = basicAlpha()
bb = basicBeta()
bb1 = basicBeta()
bd = basicDelta()
bd1 = basicDelta()
be = basicEpsilon()
be1 = basicEpsilon()
HL = HiLo(netDict)
HO1 = HiOpt1(netDict)
HO2 = HiOpt2(netDict)
K = KO(netDict)
HV = Halves(netDict)
O = Omega2(netDict)
R7 = Red7(netDict)
Z = Zen(netDict)

#initialize a game
g = game()
#add all players
g.addPlayer(d)
g.addPlayer(d1)
g.addPlayer(ba)
g.addPlayer(ba1)
g.addPlayer(bb)
g.addPlayer(bb1)
g.addPlayer(bd)
g.addPlayer(bd1)
g.addPlayer(be)
g.addPlayer(be1)
g.addPlayer(HL)
g.addPlayer(HO1)
g.addPlayer(HO2)
g.addPlayer(K)
g.addPlayer(HV)
g.addPlayer(O)
g.addPlayer(R7)
g.addPlayer(Z)
cNet = network(lr = .5, inputs = ['HiLo', 'KO', 'HiOpt1', 'HiOpt2', 'Halves', 'Omega2', 'Red7', 'Zen', 'Hand', 'hit', 'stay', 'Dealt'],  hidden = [20, 20, 10, 5], outputs = ['output'])
c = catcher(cNet)
c.addCounter(HL)
c.addCounter(HO1)
c.addCounter(HO2)
c.addCounter(K)
c.addCounter(HV)
c.addCounter(O)
c.addCounter(R7)
c.addCounter(Z)

g.addCatcher(c)
#run the game
try:
    g.gameLoop(numDecks = 10000)
    c.network.saveToFile('fin.nw')
except KeyboardInterrupt:
    c.network.saveToFile('fin.nw')
'''
from network import network
from layer import layer

n = network()
l = layer(size = 10)
l1 = layer(size = 10)
l2 = layer(size = 2)
out = layer(names = ['out'] )

n.addLayer(l)
n.addLayer(l1)
n.addLayer(l1)
n.addLayer(l1)
n.addLayer(l2)
n.addOutputLayer(out)

expected0 = {'out':0}
expected1 = {'out':1}

for i in xrange(0, 5000):
    n.train( [0,0,0,0,0], expected0 )
    n.train( [1,1,1,1,1], expected1 )
    print 'training run', i, 'complete'

o = n.run( [1,1,1,1,1] )
print o
o = n.run( [0,0,0,0,0] )
print o

from network import network
from layer import layer
import json
import random

n = network(lr = .3, inputs = ['top', 'bottom'],  hidden = [5, 5], outputs = ['output'])
for i in range(10000):
    o1 = n.train([1, 0], [1])
    o2 = n.train([0, 1], [1])
    o3 = n.train([1, 1], [0])
    o4 = n.train([0, 0], [0])
    
print '1, 0', n.run([1, 0])['output']
print '0, 1', n.run([0, 1])['output']
print '0, 0', n.run([0, 0])['output']
print '1, 1', n.run([1, 1])['output']
'''
