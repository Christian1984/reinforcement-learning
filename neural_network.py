import random

class Layer:
    def __init__(self, size):
        self.size = size

    def process(self, input):
        if (input < -1):
            return -1
        elif (input > 1):
            return 1
        
        return input

    def copy(self):
        return

class NeuralNetwork:
    def __init__(self, sizeIn, sizeHidden, sizeOut, weightsInHidden = None, weightsHiddenOut = None):
        self.rand = random.Random()
        
        self.inLayer = Layer(sizeIn)
        self.hiddenLayer = Layer(sizeHidden)
        self.outLayer = Layer(sizeOut)
        
        self.weightsInHidden = weightsInHidden if weightsInHidden is not None else self.__generateWeights(sizeIn, sizeHidden)
        self.weightsHiddenOut = weightsHiddenOut if weightsHiddenOut is not None else self.__generateWeights(sizeHidden, sizeOut)

    def mutate(self, rate):
        totalMutations = self.__mutateWeights(rate, self.weightsInHidden)
        totalMutations += self.__mutateWeights(rate, self.weightsHiddenOut)

        return totalMutations

    def clone(self):
        ihWeightsClone = self.__cloneWeights(self.weightsInHidden)
        hoWeightsClone = self.__cloneWeights(self.weightsHiddenOut)

        nnClone = NeuralNetwork(self.inLayer.size, self.hiddenLayer.size, self.outLayer.size, ihWeightsClone, hoWeightsClone)
        
        return nnClone

    def dump(self):
        return {
            "numIn": self.inLayer.size,
            "numHidden": self.hiddenLayer.size,
            "numOut": self.outLayer.size,
            "weightsInHidden": self.weightsInHidden,
            "weightsHiddenOut": self.weightsHiddenOut
        }

    ## private methods
    def __generateWeights(self, numIn, numOut):
        rows = []

        for _ in range(numIn):
            row = []

            for _ in range(numOut):
                weight = self.__randomizedWeight()
                row.append(weight)

            rows.append(row)

        return rows

    def __randomizedWeight(self):
        return self.rand.random() * (-1 if self.rand.random() < 0.5 else 1)

    def __mutateWeights(self, rate, weights):
        mutationsCount = 0

        for i in range(len(weights)):
            for j in range(len(weights[i])):
                if(self.rand.random() < rate):
                    weights[i][j] = self.__randomizedWeight()
                    mutationsCount += 1

        return mutationsCount

    def __cloneWeights(self, weights):
        rows = []

        for i in range(len(weights)):
            row = []

            for j in range(len(weights[i])):
                row.append(weights[i][j])

            rows.append(row)

        return rows

    def predict(self, input):
        if (len(input) != self.inLayer.size):
            return 0

        inOut = self.__processLayer(input, self.inLayer)
        hiddenIn = self.__processWeights(inOut, self.hiddenLayer, self.weightsInHidden)
        hiddenOut = self.__processLayer(hiddenIn, self.hiddenLayer)
        outIn = self.__processWeights(hiddenOut, self.outLayer, self.weightsHiddenOut)
        out = self.__processLayer(outIn, self.outLayer)

        return out

    def __processWeights(self, input, layer, weights):
        if len(input) != len(weights) or layer.size != len(weights[0]):
            print("processWeights: matrix does not match input and output")
            return 0

        processed = []

        for i in range(layer.size):
            res = 0

            for j in range(len(weights)):
                res += weights[j][i] * input[j]

            processed.append(res)

        return processed

    def __processLayer(self, input, layer):
        if (len(input) != layer.size):
            print("processNodes: input and nodes arrays do not match!")
            return 0

        processed = []

        for i in range(len(input)):
            processed.append(layer.process(input[i]))

        return processed