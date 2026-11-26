import alchemy.grimoire.light_spellbook as spells


def validate_ingredients(ingredients: str) -> str:
    ingredient_list: list[str] = spells.light_spell_allowed_ingredients()
    for ingredient in ingredient_list:
        if ingredient in ingredients.lower():
            return "VALID"
    return "INVALID"
