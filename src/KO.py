#TODO: add the initial running count, since unbalanced
from counter import counter
class KO(counter):
    def __init__(self, netDict = None):
        counter.__init__(self, netDict = netDict)
        self.strategy = 'KO'
        self.name = self.strategy
        self.countMap = {
                '2': 1,
                '3': 1,
                '4': 1,
                '5': 1,
                '6': 1,
                '7': 1,
                '8': 0,
                '9': 0,
                '10': -1,
                '11': -1
               }
