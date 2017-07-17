import neuron

#layer of a neural network
class layer(object):
    def __init__(self, size = None, names = None):
        #add a layer of neurons with just a size
        if size is not None:
            self.neurons = [ neuron() ] * size
        else:
            #add neurons with names
            for n in names:
                self.neurons.append( neuron(n) )
        #bias for this layer
        self.bias = 0.0
    #run the layer 
    def run(self):
        for n in self.neurons:
            n.run(self.bias)
    
    #connect layer to previous and next layers
    def connectLayer(self, pLayer = None, nLayer = None):
        for n in self.neurons:
            n.connect(pLayer, nLayer)
