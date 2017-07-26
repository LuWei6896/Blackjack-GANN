from player import player

#ballsy player - hits until it gets 19
class basicEpsilon(player):
    def __init__(self):
        player.__init__(self)
        #name for debugging/logging
        self.name = 'Basic Epsilon (Hit Until 19)'

    def play(self, deck, dealer, table = None, catcher = None, trainMethod = None):
        while not self.isStaying():
            prevCount = self.getCount()
            decision = None
            if self.getCount() <= 18:
                self.hit(deck)
                decision = 'hit'
            else:
                self.stay()
                decision = 'stay'

            if catcher is not None:
                dealtCard = self.getCount() - prevCount
                move = None
                if decision is 'hit':
                    move = 1
                else:
                    move = 0
                
                catcher.train(prevCount, move, dealtCard, [int(self.isCounting)])

            self.checkBust()
            return self.getCount()

