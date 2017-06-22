from deck import deck
from dealer import dealer
from game import game
from basicAlpha import basicAlpha



d = deck()

print 'cards in deck: ', d


deal = dealer()
ba = basicAlpha()

g = game()
g.addPlayer(ba)
g.gameLoop()

