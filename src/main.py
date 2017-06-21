from deck import deck
from dealer import dealer
from game import game


d = deck()

print 'cards in deck: ', d


deal = dealer()

g = game()
g.addPlayer(deal)
g.gameLoop()

