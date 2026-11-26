

def main() -> None:
    print("=== Kaboom 1 ===")
    print("Acess to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN EXCEPTION")
    import alchemy.grimoire.dark_spellbook as grimoire
    string = grimoire.dark_spell_record("Sauron", "bats")
    print(string)


if __name__ == "__main__":
    main()
