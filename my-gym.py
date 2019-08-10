import gym
import time

start = time.time()

envs = []

for _ in range(1000):
    envs.append([gym.make('CartPole-v0'), 0, False])

for episode in range(10):

    for env in envs:
        env[1] = env[0].reset()

    for t in range(100):
        for env in envs:
            if (not env[2]):
                #env[0].render()
                print (env[1])
                observation, reward, done, info = env[0].step(env[0].action_space.sample())
                env[1] = observation
                env[2] = done
                #observation, reward, done, info = env.step(0) #left
                #observation, reward, done, info = env.step(1) #right

                if (done):
                    print ("Episode {} finished in {} steps.".format(episode + 1, t + 1))

for env in envs:
    env[0].close()

print('done! execution took {} seconds'.format(time.time() - start))