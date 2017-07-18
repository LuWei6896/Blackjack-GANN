from layer import layer
from neuron import neuron
from util import util

class network(object):
    def __init__(self, lr = None):
        self.learningRate = lr if lr else 0.5

        self.layers = []

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
        out = [(x.name, x.output) for x in self.layers[-1].neurons]
        print out
        return out

    def train(self, inputs, expected):
        self.run(inputs)
        self.layers[-1].train(self.learningRate, expected)
        for l in reversed(self.layers[:-1]):
            l.train(self.learningRate)
