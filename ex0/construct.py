import sys
import os


def check_venv() -> bool:
  if sys.prefix != sys.base_prefix:
    return True
  else:
    return False

def get_env_name() -> str:
  


if __name__ == "__main__":
  is_venv: bool = check_venv()
  if is_venv:
    print("LABORATORY STATUS: The laboratory is sealed")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {}")
  else:
    print("LABORATORY STATUS: You are working in the open")
    print(f"Current Python: {sys.executable}")