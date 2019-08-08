from neural_network import NeuralNetwork

class Player:
    def __init__(self, brain, env):
        self.fitness = 0
        self.alive = True

        self.brain = brain
        self.env = env
        self.info = []

        self.observation = env.reset() if env else None

    @staticmethod
    def makeBaby(mom, dad, env):
        nn = NeuralNetwork.combine(mom.brain, dad.brain)
        return Player(nn, env)

    def step(self):
        if (self.alive and self.env):
            #action = self.env.action_space.sample()
            action = self.brain.predict(self.observation)

            observation, reward, done, info = self.env.step(action) #TODO

            self.observation = observation
            self.fitness += reward
            self.info.append(info)

            if (done):
                self.alive = False
        return

    def mutate(self, rate):
        self.brain.mutate(rate)
        return

    def dump(self):
        return {
            "alive": self.alive,
            "fitness": self.fitness,
            "observation": self.observation,
            "brain": self.brain.dump(),
            "info": self.info
        }