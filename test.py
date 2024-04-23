from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import COMPLEX_MOVEMENT

env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = JoypadSpace(env, COMPLEX_MOVEMENT)

def build_single_env(env_name, image_size, seed):
    env = gym_super_mario_bros.make(env_name, render_mode="human", apply_api_compatibility=True) # full_action_space=False, frameskip=1
    env = env_wrapper.SeedEnvWrapper(env, seed=seed)
    env = env_wrapper.MaxLast2FrameSkipWrapper(env, skip=4)
    # env = gymnasium.wrappers.ResizeObservation(env, shape=image_size)
    env = env_wrapper.LifeLossInfo(env)
    return env

terminated = True
for step in range(5000):
    if terminated:
        observation = env.reset()
    observation, reward, terminated, truncated, info = env.step(env.action_space.sample())
    env.render()

env.close()