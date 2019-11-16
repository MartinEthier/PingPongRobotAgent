from gym.envs.registration import register

register(id='pingpongrobot-v0',
        entry_point='pong_pong_robot.envs:PingpongrobotEnv'
        )