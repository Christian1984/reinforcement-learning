from neural_network import NeuralNetwork

nn = NeuralNetwork(2, 4, 1)
res = nn.predict([1, 2])

print(res)