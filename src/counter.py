import tensorflow as tf
from player import player



class counter(player):
    def __init__(self, network = None):
        self.network = network
        self.count = None
        self.countMap = None
        self.sess = tf.Session()

    def setCountMap(self, cm):
        self.countMap = cm

    def getNetwork(self):
        return self.network

    def setNetwork(self, network):
        self.network = network

    def predict(self):
        return

    def play(self, deck, dealer, table):
        while not self.isStaying():
            c = self.getCount(dealer, table)
            self.stay()

            
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
