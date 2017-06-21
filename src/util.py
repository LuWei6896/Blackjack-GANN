

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
