from bd_models.models import Ball, BallInstance, Player
from bd_models.models import balls as balls_cache
from bd_models.models import specials
from ballsdex.core.utils.transformers import BallTransform, BallInstanceTransform, BallEnabledTransform, SpecialEnabledTransform
from ballsdex.core.utils import checks
from ballsdex.settings import settings

from typing import Dict

def abilitymod(bossball, attacker_ball) -> Dict[str, float]:
    """
    Return multipliers or additive modifiers based on boss identity and the attacking/defending ball.
    Example return: {"atk_mult": 1.2, "hp_mult": 0.9, "atk_add": 10, "hp_add": -5}
    Inspect bossball.ball.country, bossball.special_id, attacker_ball.ball.country, attacker_ball.special_id, etc.
    """

    # defaults
    mods = {"atk_mult": 1.0, "hp_mult": 1.0, "atk_add": 0, "hp_add": 0}

    if bossball.country == "Iron":
        metalids = [2,3,5,6,7,9,12]
        if attacker_ball.ball.regime_id in metalids:
            mods["atk_mult"] = 0

    if bossball.country == "Lead":
        if attacker_ball.ball.regime_id == 19:
            mods["hp_mult"] = 1/3

    return mods
