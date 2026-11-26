import alchemy.grimoire.light_spellbook as grimoire


def main() -> None:
  string = grimoire.light_spell_record("Leviosa", "rings, mordor")
  print(string)


if __name__ == "__main__":
  main()