from layer import layer
import json
from neuron import neuron
from util import util

class network(object):
    def __init__(self, lr = None):
        self.learningRate = lr if lr else 0.5

        self.layers = []

    def __str__(self):
        return str([str(l) for l in self.layers])

    def addLayer(self, size):
        self.layers.append(layer(size = size))

    def addOutputLayer(self, names):
        self.layers.append(layer(names = names))
        self.connect()
    
    def connect(self):
        self.layers[0].connect(forward = self.layers[1].neurons)
        self.layers[-1].connect(backward = self.layers[-2].neurons)
        for i in range(len(self.layers) - 2):
            self.layers[i + 1].connect(forward = self.layers[i + 2].neurons, backward = self.layers[i].neurons)

    def run(self, values):
        self.layers[0].run(values)
        for i in range(len(self.layers) - 1):
            self.layers[i + 1].run()
        output = [(x.name, x.output) for x in self.layers[-1].neurons]
        return output

    def train(self, inputs, expected):
        run = self.run(inputs)
        self.layers[-1].train(self.learningRate, expected)
        for l in reversed(self.layers[:-1]):
            l.train(self.learningRate)
        return run
    
    def toJSON(self):
        d = []
        for l in self.layers:
            ld = {'neurons': [], 'bias': l.bias}
            for n in l.neurons:
                ld['neurons'].append( { 'name': n.name if n.name else '', 'weights': [x for x in n.weights] })
            d.append( ld )
        j = json.dumps(d) 
        r = json.loads(j)
        return r
    
                
    def fromJSON(self, js):
        for l in js:
            self.layers.append( layer(js = l) )
        self.connect()

    def saveToFile(self, fname = 'network.nw'):
        f = open(fname, 'w')
        f.write( json.dumps( self.toJSON() ) )

    def fromFile(self, fname = 'network.nw'):
        self.fromJSON( json.loads(open(fname, 'r').readline()) )
