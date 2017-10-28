from network import network
from catcher import catcher
from deck import deck
from dealer import dealer
from game import game
from basicAlpha import basicAlpha
from basicBeta import basicBeta
from basicDelta import basicDelta
from basicEpsilon import basicEpsilon
from HiLo import HiLo
from HiOpt1 import HiOpt1
from HiOpt2 import HiOpt2
from KO import KO
from Halves import Halves
from Omega2 import Omega2
from Red7 import Red7
from Zen import Zen


netDict = {
        'lr': .08,
        'inputs': ['count', 'hand', 'dealerUp'],
        'hidden': [50, 50, 25, 20, 5],
        'outputs': ['hit', 'stay']
        }

#initialize a bunch of players
d = dealer()
d1 = dealer()
ba = basicAlpha()
ba1 = basicAlpha()
bb = basicBeta()
bb1 = basicBeta()
bd = basicDelta()
bd1 = basicDelta()
be = basicEpsilon()
be1 = basicEpsilon()
HL = HiLo(netDict)
HO1 = HiOpt1(netDict)
HO2 = HiOpt2(netDict)
K = KO(netDict)
HV = Halves(netDict)
O = Omega2(netDict)
R7 = Red7(netDict)
Z = Zen(netDict)

#initialize a game
g = game()
#add all players
g.addPlayer(d)
g.addPlayer(d1)
g.addPlayer(ba)
g.addPlayer(ba1)
g.addPlayer(bb)
g.addPlayer(bb1)
g.addPlayer(bd)
g.addPlayer(bd1)
g.addPlayer(be)
g.addPlayer(be1)
g.addPlayer(HL)
g.addPlayer(HO1)
g.addPlayer(HO2)
g.addPlayer(K)
g.addPlayer(HV)
g.addPlayer(O)
g.addPlayer(R7)
g.addPlayer(Z)
cNet = network(lr =.08, inputs = ['HiLo', 'KO', 'HiOpt1', 'HiOpt2', 'Halves', 'Omega2', 'Red7', 'Zen', 'Hand', 'hit', 'stay'],  hidden = [50, 50, 20, 5], outputs = ['output'])
c = catcher(cNet)
c.addCounter(HL)
c.addCounter(HO1)
c.addCounter(HO2)
c.addCounter(K)
c.addCounter(HV)
c.addCounter(O)
c.addCounter(R7)
c.addCounter(Z)

g.addCatcher(c)
#run the game
try:
    g.gameLoop(numDecks = 10000)
    c.network.saveToFile('fin.nw')
except KeyboardInterrupt:
    c.network.saveToFile('fin.nw')
