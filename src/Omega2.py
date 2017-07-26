
from counter import counter
class Omega2(counter):
    def __init__(self, netDict = None):
        counter.__init__(self, netDict = netDict)
        self.strategy = 'Omega2'
        self.name = self.strategy
        self.countMap = {
                '2': 1,
                '3': 1,
                '4': 2,
                '5': 2,
                '6': 2,
                '7': 1,
                '8': 0,
                '9': -1,
                '10': -2,
                '11': 0
               }
