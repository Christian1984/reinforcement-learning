import random

from helper import clamp

from player import Player
from neural_network import NeuralNetwork

class Population:
    def __init__(self, envs, bestPlayersToKeepFactor = 0.01, solvedFitness = None, mutationRate = 0.02):
        self.players = [Player(NeuralNetwork(4, 8, 1), env) for env in envs]
        self.envs = envs
        self.alive = len(envs)
        self.bestPlayersToKeepFactor = clamp(bestPlayersToKeepFactor, 0, 1)
        self.solvedFitness = solvedFitness
        self.mutationRate = mutationRate
        
        self.stepsSurvived = 0
        self.populationSurvivors = 0

    def update(self):
        if self.isAlive():
            self.stepsSurvived += 1

        for player in self.players:
            alive = player.alive
            player.update()
            
            # if player died this time, update counter
            if alive and not player.alive:
                self.alive -= 1

    def isAlive(self):
        return self.alive > 0
    
    def render(self):
        for player in self.players:
            if player.alive:
                player.render()
                return
    
    def evolve(self):
        self.populationSurvivors = 0

        nextGeneration = []
        nPlayersToKeep = len(self.players) * self.bestPlayersToKeepFactor

        # sort players by fitness
        self.players.sort(key = lambda player: player.fitness, reverse = True)

        # calculate total fitness
        totalFitness = self.__calculateTotalFitness()

        for i in range(len(self.players)):
            # pick N best to keep
            newPlayer = None

            if i < nPlayersToKeep or self.players[i].hasSolvedGym(self.solvedFitness):
                self.populationSurvivors += 1
                newPlayer = Player(self.players[i].brain.clone(), self.envs[i])
            else:
                # make babies and mutate:
                # pick parents
                mom = self.__weightedRandomPick(totalFitness)
                dad = self.__weightedRandomPick(totalFitness)

                # make baby
                baby = Player.makeBaby(mom, dad, self.envs[i])

                # mutate baby
                baby.mutate(self.mutationRate)
                newPlayer = baby

            nextGeneration.append(newPlayer)
        
        # finish up
        self.players = nextGeneration
        self.alive = len(self.players)
        self.stepsSurvived = 0
    
    def stats(self):
        totalFitness = self.__calculateTotalFitness()
        averageFitness = totalFitness / len(self.players)
        return "Population survived for {} steps | Total Fitness: {} | Average Fitness: {} | Survivors from Previous Population: {}".format(
            self.stepsSurvived, totalFitness, averageFitness, self.populationSurvivors)

    def __calculateTotalFitness(self):
        return sum([player.fitness for player in self.players])

    def __weightedRandomPick(self, totalFitness):
        runningSum = 0

        for player in self.players:
            runningSum += player.fitness

            if random.uniform(0, totalFitness) <= runningSum:
                return player
        
        return self.players[0]

