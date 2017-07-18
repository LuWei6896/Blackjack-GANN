

class util(object):
    @staticmethod
    def sliceList(input, size):
        inputSize = len(input)
        sliceSize = inputSize / size
        remain = inputSize % size
        result = []
        iterator = iter(input)
        for i in range(size):
            result.append([])
            for j in range(sliceSize):
                result[i].append(iterator.next())
            if remain:
                result[i].append(iterator.next())
                remain -= 1
        return result

    @staticmethod
    def getWeightFromNeuron(nI, nO):
        c = 0
        for n in nO.getInputNeurons():
            if n is nI:
                break
            else:
                c = c + 1
        return nO.getWeightForPosition(c)

    @staticmethod
    def updateDerivative(n, nO):
        n.deriv = n.deriv + (nO.deriv * util.getWeightFromNeuron(n, nO) * n.activateDerivative() )

