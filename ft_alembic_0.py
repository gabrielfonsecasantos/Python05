import elements


def using_create_fire() -> str:
    output = elements.create_fire()
    return output


if __name__ == "__main__":
    print("=== Alembic 0 ===")
    print("Using 'import ...' structure to access elements.py")
    try:
        create_fire = using_create_fire()
        print(f"Testing create_fire: {create_fire}")
    except AttributeError as e:
        print(f"Error: {e}")
