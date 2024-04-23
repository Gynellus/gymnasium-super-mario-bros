from joypad_space import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import RIGHT_ONLY
from time import sleep

env = gym_super_mario_bros.make('SuperMarioBrosProgressiveStages-v3', rom_mode = "vanilla", render_mode = "human")
env = JoypadSpace(env, RIGHT_ONLY)

terminated = True
for step in range(5000):
    if terminated:
        observation = env.reset()
    observation, reward, terminated, truncated, info = env.step(env.action_space.sample())

env.close()

# for world in range(1, 9):
#     for stage in range(1, 5):
#         # create the target
#         target = (world, stage)
#         # setup the frame-skipping environment
#         env_id = f"SuperMarioBros-{world}-{stage}-v3"
#         print(env_id)
#         env = gym_super_mario_bros.make(env_id, rom_mode="vanilla", render_mode = "human")
#         env = JoypadSpace(env, RIGHT_ONLY)

#         terminated = True
#         for step in range(200):
#             if terminated:
#                 observation = env.reset()
#             observation, reward, terminated, truncated, info = env.step(env.action_space.sample())

#         env.close()