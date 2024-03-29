import random
import math

from helper import clamp

def trigonometricFunction(input):
    return math.tanh(input * math.pi / 2)

def linearFunction(input):
    return input

class Layer:
    def __init__(self, size, activationFunction = trigonometricFunction):
        self.size = size
        self.activationFunction = activationFunction

    def process(self, input):
        if (input < -1):
            return -1
        elif (input > 1):
            return 1
        
        return clamp(self.activationFunction(input))

class NeuralNetwork:
    def __init__(self, sizeIn, sizeHidden, sizeOut, 
        weightsInHidden = None, weightsHiddenOut = None,
        layerInActivationFunction = trigonometricFunction, 
        layerHiddenActivationFunction = trigonometricFunction,
        layerOutActivationFunction = trigonometricFunction):
        self.rand = random.Random()
        
        self.inLayer = Layer(sizeIn, layerInActivationFunction)
        self.hiddenLayer = Layer(sizeHidden, layerHiddenActivationFunction)
        self.outLayer = Layer(sizeOut, layerOutActivationFunction)
        
        self.weightsInHidden = weightsInHidden if weightsInHidden is not None else self.__generateWeights(sizeIn, sizeHidden)
        self.weightsHiddenOut = weightsHiddenOut if weightsHiddenOut is not None else self.__generateWeights(sizeHidden, sizeOut)

    # static methods
    @staticmethod
    def combine(nn1, nn2):
        if (nn1 is None or nn2 is None):
            print("Can't combine networks. Reason: One network is Null!")
            return None

        if (nn1.inLayer.size != nn2.inLayer.size 
            or nn1.hiddenLayer.size != nn2.hiddenLayer.size
            or nn1.outLayer.size != nn2.outLayer.size):
            print("Can't combine networks. Reason: Layer sizes don't match!")
            return None
        
        if (nn1.inLayer.activationFunction != nn2.inLayer.activationFunction):
            print("Can't combine networks. Reason: Activation functions don't match!")
            return None

        # combine weights by calculating the avarage of each matrix element
        weightsInHidden = [[(x + y) / 2 for x, y in zip(row1, row2)] for row1, row2 in zip(nn1.weightsInHidden, nn2.weightsInHidden)]
        weightsHiddenOut = [[(x + y) / 2 for x, y in zip(row1, row2)] for row1, row2 in zip(nn1.weightsHiddenOut, nn2.weightsHiddenOut)]

        # init new brain
        nn = NeuralNetwork(nn1.inLayer.size, 
            nn1.hiddenLayer.size, 
            nn1.outLayer.size,
            weightsInHidden, weightsHiddenOut,
            nn1.inLayer.activationFunction,
            nn1.hiddenLayer.activationFunction,
            nn1.outLayer.activationFunction)

        return nn

    # public methods
    def predict(self, input):
        if (len(input) != self.inLayer.size):
            return 0

        inOut = self.__processLayer(input, self.inLayer)
        hiddenIn = self.__processWeights(inOut, self.hiddenLayer, self.weightsInHidden)
        hiddenOut = self.__processLayer(hiddenIn, self.hiddenLayer)
        outIn = self.__processWeights(hiddenOut, self.outLayer, self.weightsHiddenOut)
        out = self.__processLayer(outIn, self.outLayer)

        return out
    
    def mutate(self, rate):
        totalMutations = self.__mutateWeights(rate, self.weightsInHidden)
        totalMutations += self.__mutateWeights(rate, self.weightsHiddenOut)

        return totalMutations

    def clone(self):
        ihWeightsClone = self.__cloneWeights(self.weightsInHidden)
        hoWeightsClone = self.__cloneWeights(self.weightsHiddenOut)

        nnClone = NeuralNetwork(self.inLayer.size, self.hiddenLayer.size, self.outLayer.size, 
            ihWeightsClone, hoWeightsClone, 
            self.inLayer.activationFunction, 
            self.hiddenLayer.activationFunction, 
            self.outLayer.activationFunction)
        
        return nnClone

    def dump(self):
        return {
            "numIn": self.inLayer.size,
            "numHidden": self.hiddenLayer.size,
            "numOut": self.outLayer.size,
            "weightsInHidden": self.weightsInHidden,
            "weightsHiddenOut": self.weightsHiddenOut
        }

    # private methods
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