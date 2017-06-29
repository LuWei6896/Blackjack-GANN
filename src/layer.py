from neuron import neuron

class layer(object):
    def __init__(self, numNeurons):
        self.neurons = [ neuron() ] * numNeurons

    def run(self):
        for n in self.neurons:
            n.run()

    def connectForward(self, l):
        for n in self.neurons:
            n.connectForward(l)

    def connectBack(self, l):
        for n in self.neurons:
            n.connectBack(l)
