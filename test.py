from joypad_space import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import RIGHT_ONLY
from time import sleep

env = gym_super_mario_bros.make('SuperMarioBros-v0', render_mode = "human")
env = JoypadSpace(env, RIGHT_ONLY)

terminated = True
for step in range(5000):
    if terminated:
        observation = env.reset()
    observation, reward, terminated, truncated, info = env.step(env.action_space.sample())
    # sleep(0.1)

env.close()