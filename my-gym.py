import gym
import time

from population import Population

start = time.time()

render = False

populationSize = 1000
episodes = 1000
maxSteps = 1000
envs = []

for _ in range(populationSize):
    envs.append(gym.make('CartPole-v0'))

population = Population(envs)

for episode in range(episodes):
    #print("===================================")
    #print("Starting Episode {}:".format(episode))

    for step in range(maxSteps):
        if population.isAlive():
            # update
            population.update()

            if render:
                population.render()

            #if step % 10 == 0:
            #    print("Step {}: {} players still alive.".format(step, population.alive))
        else:
            # evolve and restart
            print("Episode: {} | {} ".format(episode + 1, population.stats()))
            population.evolve()
            break

for env in envs:
    env[0].close()

print("Execution finished! Took {} seconds to complete".format(time.time() - start))