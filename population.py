from player import Player
from neural_network import NeuralNetwork

class Population:
    def __init__(self, envs):
        self.players = [Player(NeuralNetwork(4, 8, 1), env) for env in envs]
        self.alive = len(envs)

    def update(self):
        for player in self.players:
            alive = player.alive
            player.update()

            # if player died this time, update counter
            if alive and not player.alive:
                self.alive -= 1
        
        if self.alive <= 0:
            self.nextGeneration()

    def nextGeneration(self):
        #TODO
        # calculate total fitness
        # pick N best to keep
        # make babies and mutate:
            # pick parents
            # make baby
            # mutate baby
        return