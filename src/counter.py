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
        
    def updateCount(self, roundDealt):
        for card in roundDealt:
            self.count += float( self.countMap[ str(card) ] )

    def getNetwork(self):
        return self.network

    def setNetwork(self, network):
        self.network = network

    def predict():
        return

    def play(deck):
        while not self.staying:
            


