from neuron import neuron
import random

#layer of a neural network
class layer(object):
    def __init__(self, size = None, names = None):
        #add a layer of neurons with just a size
        self.neurons = []
        if size is not None:
            self.neurons = [ neuron() ] * size
        else:
            #add neurons with names
            for n in names:
                self.neurons.append( neuron(n) )
        #bias for this layer
        self.bias = random.random()
    #run the layer 
    def run(self):
        for n in self.neurons:
            n.run(self.bias)
    
    #connect layer to previous and next layers
    def connectLayer(self, pLayer = None, nLayer = None):
        for n in self.neurons:
            n.connect(pLayer, nLayer)

    def getNeurons(self):
        return self.neurons

    def inputRun(self, values):
        for n, v in zip(self.neurons, values):
            n.inputRun(v)

    def applyDeltas(self):
        for n in self.neurons:
            n.applyDeltas()
 
    def train(self, expected, lr):
        
        for i, n in enumerate(self.neurons):
            self.neurons[i].train(expected, lr)
        sm = 0.0
        for n in self.neurons:
            sm = sm + n.deriv
        #print 'sum of all derivs', sm
        #print 'bias', self.bias
        
        self.bias = self.bias - (lr * sm)
        #print 'new bias', self.bias
