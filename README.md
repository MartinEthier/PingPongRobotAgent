# PingPongRobotAgent
This repository is a project involving simulating and training a robotic arm to play the game of ping pong. The simulator is created using the PyBullet environment and a reinforcement learning agent is trained with OpenAI's gym library.

## Simulation
A gym environment called ping-pong-robot is created with PyBullet. This environment was based on the environment found in the following repository: https://github.com/yconst/balance-bot. Changes were made to convert from a balancing bot to a robot arm.

## Agent
The agent was trained with the use of PyTorch and the gym environment. The deep reinforcement learning model used is proximal policy optimization (PPO).
