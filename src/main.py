from deck import deck
from dealer import dealer
from game import game
from basicAlpha import basicAlpha
from basicBeta import basicBeta


d = deck()

print 'cards in deck: ', d


deal = dealer()
ba = basicAlpha()
bb = basicBeta()

g = game()
g.addPlayer(ba)
g.addPlayer(bb)
g.gameLoop()

