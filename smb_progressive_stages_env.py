"""An OpenAI Gym environment for Super Mario Bros. and Lost Levels."""
from collections import defaultdict
from .smb_env import SuperMarioBrosEnv
import numpy as np
from ._roms import decode_target
from ._roms import rom_path

class SuperMarioBrosProgressiveStagesEnv(SuperMarioBrosEnv):
    """An environment for playing Super Mario Bros with OpenAI Gym."""

    # relevant meta-data about the environment
    metadata = SuperMarioBrosEnv.metadata

    # the legal range of rewards for each step
    reward_range = SuperMarioBrosEnv.reward_range

    # observation space for the environment is static across all instances
    observation_space = SuperMarioBrosEnv.observation_space

    # action space is a bitmap of button press values for the 8 NES buttons
    action_space = SuperMarioBrosEnv.action_space

    def __init__(self, rom_mode='vanilla', render_mode = "human", **kwargs):
        
        # create a dedicated random number generator for the environment
        self.np_random = np.random.RandomState()
        # setup the environments
        self.envs = []
        # iterate over the worlds in the game, i.e., {1, ..., 8}
        for world in range(1, 9):
            # append a new list to put this world's stages into
            self.envs.append([])
            # iterate over the stages in the world, i.e., {1, ..., 4}
            for stage in range(1, 5):
                # create the target as a tuple of the world and stage
                target = (world, stage)
                # create the environment with the given ROM mode
                env = SuperMarioBrosEnv(rom_mode=rom_mode, target=target, render_mode='rpg_array', **kwargs)
                # add the environment to the stage list for this world
                self.envs[-1].append(env)
                
        # print("Enviornments total: ", len(self.envs))

        self.render_mode = render_mode
        # create a placeholder for the current environment
        self.env = self.envs[0][0]
        self.env.render_mode = render_mode
        # self.reset()
        # print("reset done", self.env.render_mode)
        # create a placeholder for the image viewer to render the screen
        self.viewer = None
        # keep a record of the current_env
        self.current_level = (0, 0)

    def _select_next_level(self):
        """Select the following level to use."""
        world, stage = self.current_level
        print("Finished level: ", world+1, "-", stage+1)
        if stage < 4:
            stage += 1
        else:
            world += 1
            stage = 1
        self.env = self.envs[world][stage]
        self.env.render_mode = self.render_mode
        self.current_level = (world, stage)


    def seed(self, seed=None):
        """
        Set the seed for this environment's random number generator.

        Returns:
            list<bigint>: Returns the list of seeds used in this env's random
              number generators. The first value in the list should be the
              "main" seed, or the value which a reproducer should pass to
              'seed'. Often, the main seed equals the provided 'seed', but
              this won't be true if seed=None, for example.

        """
        # if there is no seed, return an empty list
        if seed is None:
            return []
        # set the random number seed for the NumPy random number generator
        self.np_random.seed(seed)
        # return the list of seeds used by RNG(s) in the environment
        return [seed]

    def reset(self, **kwargs):
        """
        Reset the state of the environment and returns an initial observation.

        Returns:
            state (np.ndarray): next frame as a result of the given action

        """ 
        return self.env.reset(**kwargs)

    def step(self, action):
        """
        Run one frame of the NES and return the relevant observation data.

        Args:
            action (byte): the bitmap determining which buttons to press

        Returns:
            a tuple of:
            - state (np.ndarray): next frame as a result of the given action
            - reward (float) : amount of reward returned after given action
            - done (boolean): whether the episode has ended
            - info (dict): contains auxiliary diagnostic information

        """
        screen, reward, terminated, truncated, info = self.env.step(action)
        if truncated:
            self._select_next_level()
        return screen, reward, terminated, truncated, info

    def close(self):
        """Close the environment."""
        # make sure the environment hasn't already been closed
        if self.env is None:
            raise ValueError('env has already been closed.')
        # iterate over each list of stages
        for stage_lists in self.envs:
            # iterate over each stage
            for stage in stage_lists:
                # close the environment
                stage.close()
        # close the environment permanently
        self.env = None
        # if there is an image viewer open, delete it
        if self.viewer is not None:
            self.viewer.close()

    def get_keys_to_action(self):
        """Return the dictionary of keyboard keys to actions."""
        return self.env.get_keys_to_action()

    def get_action_meanings(self):
        """Return the list of strings describing the action space actions."""
        return self.env.get_action_meanings()
    
    
# explicitly define the outward facing API of this module
__all__ = [SuperMarioBrosProgressiveStagesEnv.__name__]
