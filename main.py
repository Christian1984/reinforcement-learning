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