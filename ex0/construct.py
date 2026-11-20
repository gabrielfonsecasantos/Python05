import sys
import os


def check_venv() -> bool:
  if sys.prefix != sys.base_prefix:
    return True
  else:
    return False


if __name__ == "__main__":
  is_venv: bool = check_venv()
  if is_venv:
    print("LABORATORY STATUS: The laboratory is sealed")
    print(f"Current Python: {sys.executable}")
    #print(f"Virtual Environment: {}")
  else:
    print("LABORATORY STATUS: You are working in the open\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You are in the global environment!")
    print("Every reagent you install here leaks into the whole system.\n")
    print("To seal the laboratory, run:")
    print("python -m venv lab_env")
    print("source lab_env/bin/activate # On Unix")
    print("lab_env\\Scripts\\activate # On Windows\n")
    print("Then run this program again.")
