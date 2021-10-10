from kaggle_environments import make
import random

env = make("rps", configuration={"episodeSteps": 1000})
env.run(['random_agent.py', 'copy_opponent_agent.py'])

env.render(mode="ipython", width=000, height=000)