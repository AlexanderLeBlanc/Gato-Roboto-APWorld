from dataclasses import dataclass

## Add deathlink later!!!
from Options import Choice, Range, Toggle, OptionGroup, PerGameCommonOptions

class RocketJumpsEnabled(Toggle):
    """
        Option for whether or not player is required to know rocket jump tricks for progression. 
        This enables tricks for entering and completing checks in heater core. 
        Several other smaller checks throughout the run require these tricks.
    """
    display_name = "Enable Rocket Jump Tricks"

class LogicDifficulty(Choice):
    """
        Vanilla: the game as it was intended
        Vanilla+: all skips that aren't glitches (early catridges in Nexus, spin jump tricks)
        Glitched: all the glitches you know and love
    """
    display_name = "Logic Difficulty"
    option_vanilla = 0
    option_vanilla_plus = 1
    option_glitched = 2
    default = 0
    
gatoroboto_option_groups = [
    OptionGroup("Logic Options", [
        RocketJumpsEnabled,
        LogicDifficulty
    ])
]

@dataclass
class GatoRobotoOptions(PerGameCommonOptions):
    rocket_jumps: RocketJumpsEnabled
    logic_difficulty: LogicDifficulty