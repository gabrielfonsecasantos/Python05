import importlib


def check_reagent(module_name: str) -> tuple[bool, str]:
    try:
        module = importlib.import_module(module_name)
    except ImportError:
        return False, "missing"
    version: str = getattr(module, "__version__", "unknown")
    return True, str(version)


def main() -> None:
    print("")