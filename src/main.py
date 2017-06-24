from deck import deck
from dealer import dealer
from game import game
from basicAlpha import basicAlpha
from basicBeta import basicBeta
from basicDelta import basicDelta
from basicEpsilon import basicEpsilon


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


g = game()
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
g.gameLoop(numDecks = 50)

