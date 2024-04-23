"""Registration code of Gym environments in this package."""
from .smb_env import SuperMarioBrosEnv
from .smb_random_stages_env import SuperMarioBrosRandomStagesEnv
from .smb_progressive_stages_env import SuperMarioBrosProgressiveStagesEnv
from .nes_env import NESEnv
from .joypad_space import JoypadSpace
from ._registration import make


# define the outward facing API of this package
__all__ = [
    make.__name__,
    SuperMarioBrosEnv.__name__,
    SuperMarioBrosRandomStagesEnv.__name__,
    SuperMarioBrosProgressiveStagesEnv.__name__,
    NESEnv.__name__,
    JoypadSpace.__name__,
]
