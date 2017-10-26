from neuron import neuron
import json
import random

#represent a layer in a neural network
class layer(object):
    def __init__(self, size = None, names = None, bias = None, js = None): #JS is for loading from a json file
        #set our bias randomly, unless loading for a file
        self.bias = bias if bias else random.random()
        self.neurons = []
        #initialize with just a number of neurons
        if size is not None:
           for i in range(size):
               self.neurons.append(neuron() )
        #initialize named neurons
        if names is not None:
            for n in names:
                self.neurons.append( neuron(name = n) )
        #initialize from a json object
        if js is not None:
            self.bias = js['bias']
            for n in js['neurons']:
                print n
                self.neurons.append( neuron(weights = n['weights'], name = n['name'] if n['name'] is not '' else None) )

    #printable information
    def __str__(self):
        return 'layer bias: ' + str(self.bias) + ', number of neurons: ' + str( len(self.neurons) )

    #run the layer
    def run(self, values = None):
        for i in range(len(self.neurons)):
            if values is None:
                self.neurons[i].run(None, bias = self.bias)
            else:
                self.neurons[i].run(values[i], bias = self.bias)
    
    #train the layer
    def train(self, lr, expected = None, noTrain = None, catcherDeltas = None):
        if expected is not None:
            for i in range(len(self.neurons)):
                self.neurons[i].train(lr, expected[i], noTrain = noTrain)
        elif catcherDeltas is not None:
            for i in range(len(self.neurons)):
                self.neurons[i].train(lr, noTrain = noTrain, catcherDeltas = catcherDeltas)
        else:
            for i in range(len(self.neurons)):
                self.neurons[i].train(lr, noTrain = noTrain)
            #train bias
            '''
            sm = 0.0
            for n in self.neurons:
                sm = sm + n.deriv
            self.bias = self.bias - (lr * sm)
            '''
    #connect the layer to previous and next layers
    def connect(self, backward = None, forward = None):
        for i in range(len(self.neurons)):
            self.neurons[i].connect(backward = backward, forward = forward)

