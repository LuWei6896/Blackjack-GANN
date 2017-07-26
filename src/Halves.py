
from counter import counter
class Halves(counter):
    def __init__(self, netDict = None):
        counter.__init__(self, netDict = netDict)
        self.strategy = 'Halves'
        self.name = self.strategy
        self.countMap = {
                '2': 0.5,
                '3': 1,
                '4': 1,
                '5': 1.5,
                '6': 1,
                '7': 0.5,
                '8': 0,
                '9': -0.5,
                '10': -1,
                '11': -1
               }
