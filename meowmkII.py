import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import pydot
import gym

def solve(obs):
    th,w=obs[2:4]
    if abs(th) < 0.03:
        return 0 if w<0 else 1
    else:
        return 0 if th<0 else 1

def omega(obs):
    w=obs[3]
    return 0 if w<0 else 1

def theta(obs):
    th=obs[2]
    return 0 if abs(th)<0.03 else 1

for a in range(1,6):
    env = gym.make('CartPole-v0')
    Kx=[]
    Ky=[]
    av=0
    for i in range(200):
        env.reset()
        rewards=0
        action = env.action_space.sample()
        for t in range(300):
            #env.render()
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
            action=solve(observation)
        env.close()
    plt.clf()
    plt.plot(Kx,Ky)
    plt.title("attempt "+str(a)+" aver:"+str(av/200))
    plt.xlabel("times")
    plt.ylabel("rewards")
    plt.show()