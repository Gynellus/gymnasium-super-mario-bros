"""Registration code of gymnasium environments in this package."""
import gymnasium


def _register_mario_env(id, is_random=False, is_progressive=False, **kwargs):
    """
    Register a Super Mario Bros. (1/2) environment with OpenAI gymnasium.

    Args:
        id (str): id for the env to register
        is_random (bool): whether to use the random levels environment
        kwargs (dict): keyword arguments for the SuperMarioBrosEnv initializer

    Returns:
        None

    """
    # if the is random flag is set
    if is_random:
        # set the entry point to the random level environment
        entry_point = 'gym_super_mario_bros:SuperMarioBrosRandomStagesEnv'
    elif is_progressive:
        # set the entry point to the progressive level environment
        entry_point = 'gym_super_mario_bros:SuperMarioBrosProgressiveStagesEnv'
    else:
        # set the entry point to the standard Super Mario Bros. environment
        entry_point = 'gym_super_mario_bros:SuperMarioBrosEnv'
    # register the environment
    gymnasium.envs.registration.register(
        id=id,
        entry_point=entry_point,
        max_episode_steps=9999999,
        reward_threshold=9999999,
        kwargs=kwargs,
        nondeterministic=True,
    )


# Super Mario Bros.
_register_mario_env('SuperMarioBros-v0', rom_mode='vanilla')
_register_mario_env('SuperMarioBros-v1', rom_mode='downsample')
_register_mario_env('SuperMarioBros-v2', rom_mode='pixel')
_register_mario_env('SuperMarioBros-v3', rom_mode='rectangle')


# Super Mario Bros. Random Levels
_register_mario_env('SuperMarioBrosRandomStages-v0', is_random=True, rom_mode='vanilla')
_register_mario_env('SuperMarioBrosRandomStages-v1', is_random=True, rom_mode='downsample')
_register_mario_env('SuperMarioBrosRandomStages-v2', is_random=True, rom_mode='pixel')
_register_mario_env('SuperMarioBrosRandomStages-v3', is_random=True, rom_mode='rectangle')


# Super Mario Bros. Progressive Stages
_register_mario_env('SuperMarioBrosProgressiveStages-v0', is_progressive=True, rom_mode='vanilla')
_register_mario_env('SuperMarioBrosProgressiveStages-v1', is_progressive=True, rom_mode='downsample')
_register_mario_env('SuperMarioBrosProgressiveStages-v2', is_progressive=True, rom_mode='pixel')
_register_mario_env('SuperMarioBrosProgressiveStages-v3', is_progressive=True, rom_mode='rectangle')


# Super Mario Bros. 2 (Lost Levels)
_register_mario_env('SuperMarioBros2-v0', lost_levels=True, rom_mode='vanilla')
_register_mario_env('SuperMarioBros2-v1', lost_levels=True, rom_mode='downsample')


def _register_mario_stage_env(id, **kwargs):
    """
    Register a Super Mario Bros. (1/2) stage environment with OpenAI gymnasium.

    Args:
        id (str): id for the env to register
        kwargs (dict): keyword arguments for the SuperMarioBrosEnv initializer

    Returns:
        None

    """
    # register the environment
    gymnasium.envs.registration.register(
        id=id,
        entry_point='gym_super_mario_bros:SuperMarioBrosEnv',
        max_episode_steps=9999999,
        reward_threshold=9999999,
        kwargs=kwargs,
        nondeterministic=True,
    )


# a template for making individual stage environments
_ID_TEMPLATE = 'SuperMarioBros{}-{}-{}-v{}'
# A list of ROM modes for each level environment
_ROM_MODES = [
    'vanilla',
    'downsample',
    'pixel',
    'rectangle'
]


# iterate over all the rom modes, worlds (1-8), and stages (1-4)
for version, rom_mode in enumerate(_ROM_MODES):
    for world in range(1, 9):
        for stage in range(1, 5):
            # create the target
            target = (world, stage)
            # setup the frame-skipping environment
            env_id = _ID_TEMPLATE.format('', world, stage, version)
            _register_mario_stage_env(env_id, rom_mode=rom_mode, target=target)


# create an alias to gymnasium.make for ease of access
make = gymnasium.make


# define the outward facing API of this module (none, gymnasium provides the API)
__all__ = [make.__name__]
