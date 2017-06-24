from player import player


class basicEpsilon(player):
    def __init__(self):
        player.__init__(self)
        self.name = 'Basic Epsilon (Hit Until 19)'

    def play(self, deck, dealer):
        while not self.isStaying():
            if self.getCount() <= 18:
                self.hit(deck)
            else:
                self.stay()

            self.checkBust()
            return self.getCount()

