import alchemy.transmutation.recipes as recipe


if __name__ == "__main__":
    print("=== Transmutation 0 ===")
    print("Using file alchemy/trasmutation/recipes.py directly")
    try:
        print(f"Testing lead to gold: {recipe.lead_to_gold()}")
    except Exception as e:
        print(f"Error: {e}")
