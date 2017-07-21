from layer import layer
import json
from neuron import neuron
from util import util

#neural network class
class network(object):
    def __init__(self, lr = None, inputs = None,  hidden = None, outputs = None, file = None):
        #learning rate
        self.learningRate = lr if lr else 0.5

        self.layers = []
        #for creating a network by naming inputs, outputs, and hidden layer dims
        if hidden is not None:
            self.addInputLayer(inputs)
            for v in hidden:
                self.addLayer(v)
            self.addOutputLayer(outputs)
            self.connect()
        #load from file 
        if file is not None:
            self.fromFile(file = file)

    #print the network info
    def __str__(self):
        return str([str(l) for l in self.layers])
   
    #add layer of input neurons
    def addInputLayer(self, names):
        self.layers.append( layer(names = names) )

    #add hidden layer
    def addLayer(self, size):
        self.layers.append(layer(size = size))

    #add a layer of output neurons
    def addOutputLayer(self, names):
        self.layers.append(layer(names = names))
        self.connect()
   
    #connect all network layers to eachother
    def connect(self):
        self.layers[0].connect(forward = self.layers[1].neurons)
        self.layers[-1].connect(backward = self.layers[-2].neurons)
        for i in range(len(self.layers) - 2):
            self.layers[i + 1].connect(forward = self.layers[i + 2].neurons, backward = self.layers[i].neurons)
    #run the network
    def run(self, values):
        #run the input layer with values
        self.layers[0].run(values)
        #run rest of layers which will feedforward
        for i in range(len(self.layers) - 1):
            self.layers[i + 1].run()
        output = {}
        #store output in a dict
        for x in self.layers[-1].neurons:
            output[x.name] = x.output
        return output

    #train the network 
    def train(self, inputs, expected, noTrain = None, catcher = None):
        #run the network to store activations
        run = self.run(inputs)
        #stuff for if we have a catcher network running
        crun = None
        crunInputs = []
        cDeltas = None
        #get the deltas from the catcher network so we can act like it just feeds directly off of our network
        if catcher is not None:
            for i in run:
                crunInputs.append(run[i])
            crun = catcher.run(crunInputs)
            #we want to make it so that the catcher doesnt think we are cheating (aka it outputs a 0% probability that we are cheating, hence the [0.0])
            cDeltas = catcher.getDetlas(crunInputs, [0.0])
        #train the output layer with expected outputs
        self.layers[-1].train(self.learningRate, expected, noTrain = noTrain)
        #train hidden layers backwards (backpropagate)
        for l in reversed(self.layers[:-1]):
            l.train(self.learningRate)
        #if the catcher network feeds off of this one, run another training pass in respect to the catcher output
        if catcher is not None:
            #train with catcher deltas
            self.layers[-1].train(self.learningRate, noTrain = noTrain, catcherDeltas = cDeltas)
            for l in reversed(self.layers[:-1]):
                l.train(self.learningRate, catcherDeltas = cDeltas)
        return run

    #method used to retrieve the partial derivative of the error in respect to the input neurons of the network (made specifically for the catcher network to be able to retrieve its input deltas
    def getDeltas(self, inputs, expected):
        #run to get activations
        run = self.run(inputs)
        #backpropagate without updating
        self.layers[-1].train(self.learningRate, expected, noTrain = True)
        for l in reversed(self.layers[:-1]):
            if l is self.layers[0]:
                l.train(self.learningRate, noTrain = True)
            else:
                l.train(self.learningRate, noTrain = True)
        out = {}
        #get an output dictionary
        for n in self.layers[0].neurons:
            out[n.name] = n.deriv
        return out
    
    #save the network to a json object
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
    
    #load the network from a json object 
    def fromJSON(self, js):
        for l in js:
            self.layers.append( layer(js = l) )
        self.connect()

    #save the network as a json object to a file 
    def saveToFile(self, fname = 'network.nw'):
        f = open(fname, 'w')
        f.write( json.dumps( self.toJSON() ) )

    #load the network from a json file 
    def fromFile(self, fname = 'network.nw'):
        self.fromJSON( json.loads(open(fname, 'r').readline()) )
