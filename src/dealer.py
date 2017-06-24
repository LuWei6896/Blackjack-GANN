from player import player
from deck import deck

class dealer(player):
    def __init__(self):
        player.__init__(self)
        self.holeCard = None
        self.name = 'Dealer'

    def reset(self):
        player.reset(self)
        self.holeCard = None

    def getCount(self):
        return player.getCount(self) + self.holeCard

    def hit(self, deck):
        card = deck.dealCard()
        if self.holeCard is None:
            self.holeCard = card
        else:
            self.upCards.append(card)

    def play(self, deck, dealer = None, table = None):
        while not self.isStaying():
            if self.getCount() < 17:
                self.hit(deck)
            else:
                self.stay() 
        self.checkBust() 
        return self.getCount()
    
    def getUpCard(self):
        return sum( self.upCards )
