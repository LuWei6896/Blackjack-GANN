#import tensorflow as tf
from player import player


#template class for a card counting network
class counter(player):
    #initialize the player, potentially with a neural network
    def __init__(self, network = None):
        self.network = network if network is not None else None
        self.count = None
        self.countMap = None
        #self.sess = tf.Session()
    
    #map cards to the count associated with it
    def setCountMap(self, cm):
        self.countMap = cm

    #return the network 
    def getNetwork(self):
        return self.network
    #set the network
    def setNetwork(self, network):
        self.network = network
    
    #run the network given the count, etc., etc. and get its prediction
    def predict(self):
        return
    
    #play a hand of blackjack
    def play(self, deck, dealer, table):
        while not self.isStaying():
            c = self.getCount(dealer, table)
            self.stay()

    #get the count associated with cards on the table 
    def getCount(self, dealer, table):
        count = 0.0
        arr = [x for x in table]
        arr.append(dealer)
        for p in arr:
            cards = p.getUpCards()
            for n in cards:
                count += self.countMap[ str(n) ]
        self.count = count
        return count
