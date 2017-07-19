'''
from deck import deck
from dealer import dealer
from game import game
from basicAlpha import basicAlpha
from basicBeta import basicBeta
from basicDelta import basicDelta
from basicEpsilon import basicEpsilon

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
#run the game
g.gameLoop(numDecks = 50)
'''
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
'''

from network import network
from layer import layer

n = network()
n.addLayer(5)
n.addLayer(5)
n.addLayer(5)
n.addOutputLayer(['l', 'r'])
for i in range(10000):
    n.train([1,1,1,1,1], [1.0, 0.0])
    n.train([0,0,0,0,0], [0.0, 1.0])
    #n.train([1,1,1,1,1], [1.0])
    #n.train([0,0,0,0,0], [0.0])

n.run([1,1,1,1,1])
n.toJSON()
