import gym

env = gym.make('CartPole-v0')

#print (env.action_space)
#print (env.action_space.sample())

for i_episode in range(10):
    observation = env.reset()

    for t in range(100):
        env.render()
        print (observation)
        observation, reward, done, info = env.step(env.action_space.sample())
        #observation, reward, done, info = env.step(0) #left
        #observation, reward, done, info = env.step(1) #right

        if (done):
            print ("Episode {} finished in {} steps.".format(i_episode + 1, t + 1))
            break

env.close()

print('done!')