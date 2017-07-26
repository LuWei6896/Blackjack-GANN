#TODO: add initial running count for unbalanced system
#TODO: check why seven is 0 or 1 and when to use which value
from counter import counter
class Red7(counter):
    def __init__(self, netDict = None):
        counter.__init__(self, netDict = netDict)
        self.strategy = 'Red7'
        self.name = self.strategy
        self.countMap = {
                '2': 1,
                '3': 1,
                '4': 1,
                '5': 1,
                '6': 1,
                '7': 0,#or 1
                '8': 0,
                '9': 0,
                '10': -1,
                '11': -1
               }
