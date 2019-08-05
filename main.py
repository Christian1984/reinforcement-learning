from neural_network import NeuralNetwork

nn = NeuralNetwork(4, 8, 2)

for i in range(10):
    nn.mutate(0.02)
    res = nn.predict([0.1, 0.2, 0.3, 0.4])
    print(res)