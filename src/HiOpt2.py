
from counter import counter
class HiOpt2(counter):
    def __init__(self, netDict = None):
        counter.__init__(self, netDict = netDict)
        self.strategy = 'HiOpt2'
        self.name = self.strategy
        self.countMap = {
                '2': 1,
                '3': 1,
                '4': 2,
                '5': 2,
                '6': 1,
                '7': 1,
                '8': 0,
                '9': 0,
                '10': -2,
                '11': 0
               }
