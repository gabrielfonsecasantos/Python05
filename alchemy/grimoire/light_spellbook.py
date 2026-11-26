import alchemy.grimoire.light_validator as light_validator


def light_spell_allowed_ingredients() -> list[str]:
    element_list = ["earth", "air", "fire", "water"]
    return element_list


def light_spell_record(spell_name: str, ingredients: str) -> str:
    if light_validator.validate_ingredients(ingredients) == "VALID":
        return f"Spell recorded: {spell_name} ({ingredients} - VALID)"
    else:
        return f"Spell recorded: {spell_name} ({ingredients} - INVALID)"
