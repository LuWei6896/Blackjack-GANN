from layer import layer
from inputLayer import inputLayer 

class network(object):
    def __init__(self):
        self.layers = []
        self.connected = False

    def addLayer(self, l):
        self.layers.append(l)

    def addInputLayer(self, layerSize):
        self.layers = [inputLayer(layerSize)] + self.layers

    def addOuputLayer(self, layerSize, names = None):
        if names is None:
            self.layers.append( outputLayer(layerSize) )
        else:
            self.layers.append( outputLayer(layerSize, names) )
    
    def connectAll(self):
        idx = 0
        for l in self.layers[1:]:
            l.connectBack( self.layers[idx] )
            idx = idx + 1
        idx = 1 
        for l in self.layers[:-1]:
            l.connectForward( self.layers[idx] )
            idx = idx + 1

        self.connected = True


    def run(self, inputs):
        if not self.connected:
            self.connectAll()
        self.layers[0].run(inputs)
        for layer in self.layers[1:]:
            layer.run()
        return self.layers[-1].getOutputs()
