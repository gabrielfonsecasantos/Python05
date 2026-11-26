from grimoire.light_spellbook import (
    light_spell_allowed_ingredients as allowed_ingredients)


def validate_ingredients(ingredients: str) -> str:
    ingredient_list: list[str] = allowed_ingredients()
    for ingredient in ingredient_list:
        if ingredient in ingredients.lower():
            return "VALID"
    return "INVALID"
