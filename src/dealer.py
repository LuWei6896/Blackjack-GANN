from player import player
from deck import deck

class dealer(player):
    def __init__(self):
        player.__init__(self)
        self.holeCard = None

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

    def play(self, deck):
        while not self.staying:
            print 'count is ', self.getCount()
            if self.getCount() < 17:
                print 'hitting'
                self.hit(deck)
            else:
                print 'staying'
                self.stay() 
        self.checkBust() 
        if self.bust:
            print 'busted'
        else:
            print 'did not bust'
        return self.getCount()
