import importlib


def check_reagent(module_name: str) -> tuple[bool, str]:
    try:
        module = importlib.import_module(module_name)
    except ImportError:
        return False, "missing"
    version: str = getattr(module, "__version__", "unknown")
    return True, version


def main() -> None:
    res_pandas, version_pandas = check_reagent("pandas")
    res_numpy, version_numpy = check_reagent("numpy")
    if res_pandas:
        print(f"[OK] pandas ({version_pandas}): Data manipulation ready")
    else:
        print(f"pandas: {version_pandas}")

    if res_numpy:
        print(f"[OK] numpy ({version_numpy}): Numerical computation ready")
    else:
        print(f"numpy: {version_numpy}")

    print("""
pip vs Poetry:
    requirements.txt declares what to install; pip resolves it at install time.
    pyproject.toml declares the same constraints, and Poetry pins the resolved
    versions in poetry.lock so every install is identical.
    """)

    if res_pandas and res_numpy:
        print("All reagents present and accounted for.")
    else:
        print("You have at least one missing reagent.")
        print("Install via pip: pip install -r ex0/requirements.txt")
        print("Install via Poetry: poetry install")


if __name__ == "__main__":
    main()
