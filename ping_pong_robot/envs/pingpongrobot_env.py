import os
import math
import numpy as np

import gym
from gym import spaces
from gym.utils import seeding

import pybullet as p
import pybullet_data

class PingpongrobotEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self._observation = []
        self.action_space = spaces.Discrete(9)
        # pitch, gyro, commanded speed
        self.observation_space = spaces.Box(np.array([-math.pi, -math.pi, -5]),
                                            np.array([math.pi, math.pi, 5]))
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath()) # used by loadURDF
        self._seed()

    def _seed(self, seed=None):
        pass

    def _step(self, action):
        self._assign_throttle(action)
        p.stepSimulation()
        self._observation = self._compute_observation()
        reward = self._compute_reward()
        done = self._compute_done()

        self._envStepCounter += 1

        return np.array(self._observation), reward, done, {}

    def _reset(self):
        pass

    def _assign_throttle(self, action):
        pass

    def _compute_observation(self):
        pass

    def _compute_reward(self):
        pass

    def _compute_done(self):
        pass

    def _render(self, mode='human', close=False):
        pass

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)
