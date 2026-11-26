from grimoire.light_validator import validate_ingredients as validator


def light_spell_allowed_ingredients() -> list[str]:
    element_list = ["earth", "air", "fire", "water"]
    return element_list


def light_spell_record(spell_name: str, ingredients: str) -> str:
    if validator(ingredients) == "VALID":
        print(f"Spell recorded: {spell_name} ({ingredients} - VALID)")
    else:
        print(f"Spell recorded: {spell_name} ({ingredients} - INVALID)")


if __name__ == "__main__":
    res = light_spell_record("Fantasy", "air, wind, fire")
    print(res)
