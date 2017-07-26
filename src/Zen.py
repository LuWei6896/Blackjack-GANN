
from counter import counter
class Zen(counter):
    def __init__(self, netDict = None):
        counter.__init__(self, netDict = netDict)
        self.strategy = 'Zen'
        self.name = self.strategy
        self.countMap = {
                '2': 1,
                '3': 1,
                '4': 2,
                '5': 2,
                '6': 2,
                '7': 1,
                '8': 0,
                '9': 0,
                '10': -2,
                '11': -1
               }
