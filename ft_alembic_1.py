import alchemy


def using_create_air() -> str:
    output = alchemy.create_air()
    return output


def using_create_earth() -> str:
    output = alchemy.create_earth()
    return output


if __name__ == "__main__":
    print("=== Alembic 1 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    try:
        create_air = using_create_air()
        print(f"Testing create_air: {create_air}")
        print("Now show that not all functions can be reached")
        print("This will raise an exception!")
        print("Testing the hidden create_earth:\n")
        create_earth = using_create_earth()
        print(create_earth)
    except AttributeError as e:
        print(f"AttributeError exception: {e}")
