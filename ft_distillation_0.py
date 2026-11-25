from alchemy import potions


def using_healing_potion() -> str:
    output = potions.healing_potion()
    return output


def using_strength_potion() -> str:
    output = potions.strength_potion()
    return output


if __name__ == "__main__":
    print("=== Distillation 0 ===")
    try:
        print("Direct access to alchemy/potions.py")
        print(f"Testing strenght_potion: {using_strength_potion()}")
        print(f"Testing healing_potion: {using_healing_potion()}")
    except AttributeError as e:
        print(f"Error: {e}")
