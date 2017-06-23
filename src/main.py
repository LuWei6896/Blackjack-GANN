from deck import deck
from dealer import dealer
from game import game
from basicAlpha import basicAlpha
from basicBeta import basicBeta
from basicDelta import basicDelta


d = deck()

print 'cards in deck: ', d


d = dealer()
d1 = dealer()
d2 = dealer()
ba = basicAlpha()
ba1 = basicAlpha()
ba2 = basicAlpha()
bb = basicBeta()
bb1 = basicBeta()
bb2 = basicBeta()
bd = basicDelta()
bd1 = basicDelta()
bd2 = basicDelta()

g = game()
g.addPlayer(d)
g.addPlayer(d1)
g.addPlayer(d2)
g.addPlayer(ba)
g.addPlayer(ba1)
g.addPlayer(ba2)
g.addPlayer(bb)
g.addPlayer(bb1)
g.addPlayer(bb2)
g.addPlayer(bd)
g.addPlayer(bd1)
g.addPlayer(bd2)
g.gameLoop()

