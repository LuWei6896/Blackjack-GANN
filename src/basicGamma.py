from player import player

#player to implement a betting system, not necessarily a hit/stay strategy
#to be used later in the project when we make the network more advanced, but right now it only focuses on hit/stay
class basicGamma(player):
    def __init__(self):
        player.__init__(self)
        self.name = 'Basic Gamma (1236 System)'
