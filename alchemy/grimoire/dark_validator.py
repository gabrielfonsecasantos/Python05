from alchemy.grimoire.dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    ingredient_list: list[str] = dark_spell_allowed_ingredients()
    for ingredient in ingredient_list:
        if ingredient in ingredients.lower():
            return "VALID"
    return "INVALID"
