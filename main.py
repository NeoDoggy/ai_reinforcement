import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import pydot
import gym
env = gym.make('CartPole-v0')
observation = env.reset()
Kx=[]
Ky=[]
for i in range(200):
    env.reset()
    rewards=0
    for t in range(100):
        #env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        rewards += reward
        print(observation)
        if done:
            print("Rewards: ", rewards)
            Kx.append(rewards)
            Ky.append(i)
            rewards=0
            break
    env.close()
plt.clf()
plt.plot(Kx,Ky)
plt.title("yeah")
plt.xlabel("rewards")
plt.ylabel("times")
plt.show()