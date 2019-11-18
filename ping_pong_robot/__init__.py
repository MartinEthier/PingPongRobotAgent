import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(id='pingpongrobot-v0',
         entry_point='pong_pong_robot.envs:PingpongrobotEnv')
