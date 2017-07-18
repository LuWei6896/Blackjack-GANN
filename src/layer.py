from neuron import neuron
import random


class layer(object):
    def __init__(self, size = None, names = None, bias = None):
        self.bias = bias if bias else random.random()
        self.neurons = []
        if size is not None:
           for i in range(size):
               self.neurons.append(neuron() )
        else:
            for n in names:
                self.neurons.append( neuron(name = n) )


    def run(self, values = None):
        for i in range(len(self.neurons)):
            self.neurons[i].run(values[i] if values else None, bias = self.bias)

    def train(self, lr, expected = None):
        if expected is not None:
            for i in range(len(self.neurons)):
                self.neurons[i].train(lr, expected[i])
        else:
            for i in range(len(self.neurons)):
                self.neurons[i].train(lr)
            #train bias
            sm = 0.0
            for n in self.neurons:
                sm = sm + n.deriv
            self.bias = self.bias - (lr * sm)

    def connect(self, backward = None, forward = None):
        for i in range(len(self.neurons)):
            self.neurons[i].connect(backward = backward, forward = forward)

