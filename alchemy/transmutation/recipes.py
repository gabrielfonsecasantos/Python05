from elements import create_fire
from ..elements import create_air
from alchemy.potions import strength_potion


def lead_to_gold() -> str:
    air = create_air()
    fire = create_fire()
    strength = strength_potion()
    output = (f"Recipe transmuting Lead to Gold: brew '{air}' and "
              f"'{strength}' mixed with '{fire}'")
    return output
