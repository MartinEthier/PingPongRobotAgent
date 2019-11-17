import os
import math
import numpy as np

import gym
from gym import error, spaces, utils
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

    def _step(self, action):
        pass

    def _reset(self):
        pass

    def _render(self, mode='human', close=False):
        pass

    def _seed(self, seed=None):
        pass
