import alchemy.elements  # noqa: F401
import elements  # noqa: F401


def healing_potion() -> str:
    earth = alchemy.elements.create_earth()
    air = alchemy.elements.create_air()
    output: str = f"Healing potion brewed with '{earth}' and '{air}'"
    return output


def strength_potion() -> str:
    fire = elements.create_fire()
    water = elements.create_water()
    output = f"Strength potion brewed with '{fire}' and '{water}'"
    return output
