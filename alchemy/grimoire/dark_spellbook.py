from alchemy.grimoire.dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    element_list = ["bats", "frogs", "arsenic", "eyeball"]
    return element_list


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    if validate_ingredients(ingredients) == "VALID":
        return f"Spell recorded: {spell_name} ({ingredients} - VALID)"
    else:
        return f"Spell recorded: {spell_name} ({ingredients} - INVALID)"
