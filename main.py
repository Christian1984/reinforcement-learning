from neural_network import NeuralNetwork
from player import Player

'''
nn = NeuralNetwork(4, 8, 2)
#print(nn.dump())

for i in range(10):
    mutations = nn.mutate(0.02)
    res = nn.predict([1, 2, 0.3, -0.4])
    print('{},\tmutations: {}'.format(res, mutations))

#print(nn.dump())
'''

momsBrain = NeuralNetwork(4, 8, 2)
mom = Player(momsBrain, None)

dadsBrain = NeuralNetwork(4, 8, 2)
dad = Player(dadsBrain, None)

baby = Player.makeBaby(mom, dad, None)

print(baby.dump())

print(mom.brain.weightsInHidden[0][0])
print(dad.brain.weightsInHidden[0][0])
print(baby.brain.weightsInHidden[0][0])

'''
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
B = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

C = [[(x + y) / 2 for x, y in zip(row1, row2) ] for row1, row2 in zip(A, B)]

print(C)
'''