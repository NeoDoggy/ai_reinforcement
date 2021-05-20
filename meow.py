import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import pydot
import gym
for a in range(1,6):
    env = gym.make('CartPole-v0')
    Kx=[]
    Ky=[]
    av=0
    for i in range(200):
        env.reset()
        rewards=0
        for t in range(200):
            #env.render()
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            rewards += reward
            print(observation)
            if done:
                print("Rewards: ", rewards)
                Ky.append(rewards)
                av+=rewards
                Kx.append(i)
                rewards=0
                break
        env.close()
    plt.clf()
    plt.plot(Kx,Ky)
    plt.title("attempt "+str(a)+" aver:"+str(av/200))
    plt.xlabel("times")
    plt.ylabel("rewards")
    plt.show()