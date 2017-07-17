from player import player

#ballsy player - hits until it gets 19
class basicEpsilon(player):
    def __init__(self):
        player.__init__(self)
        #name for debugging/logging
        self.name = 'Basic Epsilon (Hit Until 19)'

    def play(self, deck, dealer, table = None):
        while not self.isStaying():
            if self.getCount() <= 18:
                self.hit(deck)
            else:
                self.stay()

            self.checkBust()
            return self.getCount()

