import alchemy


def using_create_air() -> str:
    output = alchemy.create_air()
    return output


def using_create_earth() -> str:
    output = alchemy.create_earth()
    return output


if __name__ == "__main__":
    try:
        create_air = using_create_air()
        print(create_air)
        create_earth = using_create_earth()
        print(create_earth)
    except AttributeError as e:
        print(f"Error: {e}")
