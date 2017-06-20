from player import player

class dealer(player):
    def __init__(self):
        player.init()
        self.holeCard = None

    def getCount(self):
        return player.getCount() + self.holeCard

    def hit(self, deck):
        card = deck.dealCard()
        if holeCard is None:
            holeCard = card
        else:
            self.upCards.append(card)

    def play(deck):
        while not self.staying:
            if self.getCount() < 17:
                self.hit(deck)
            else:
                self.stay()
        
        return self.getCount()
