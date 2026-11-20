import sys
import os
import site


def check_venv() -> bool:
    if sys.prefix != sys.base_prefix:
        return True
    else:
        return False


def get_env_name() -> str | None:
    venv_name = os.path.basename(os.path.normpath(os.environ["VIRTUAL_ENV"]))
    if venv_name:
        return venv_name
    return None


def get_env_path() -> str | None:
    venv_path = os.environ["VIRTUAL_ENV"]
    if venv_path:
        return venv_path
    return None


def get_package_path() -> str:
    path_list: list[str] = site.getsitepackages()
    if path_list:
        path = path_list[0]
    return path


if __name__ == "__main__":
    is_venv: bool = check_venv()
    if is_venv:
        print("LABORATORY STATUS: The laboratory is sealed\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {get_env_name()}")
        print(f"Environment Path: {get_env_path()}\n")
        print("SUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting the global system.")
        print("\nReagent installation path:")
        print(f"{get_package_path()}")
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
