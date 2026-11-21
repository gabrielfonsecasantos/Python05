import os
from dotenv import load_dotenv


def load_config() -> None:
    load_dotenv()
    matrix_mode = os.getenv("MATRIX_MODE")
    db = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion = os.getenv("ZION_ENDPOINT")

    if matrix_mode == 'development':
        print("Mode: development")
    else:
        print("Mode: production")

    if not db:
        print("Not connected to local instance.")
    else:
        print("Connected to local instance.")

    if not api_key:
        print("Unauthenticated. API key missing.")
    else:
        print("Authenticated.")

    if not log_level:
        print("WARNING")
    else:
        print("DEBUG")

    if not zion:
        print("Disconnected.")
    else:
        print("Connected.")


if __name__ == "__main__":
    print("ORACLE STATUS: Consulting the configuration...\n")
    print("Configuration loaded:")
    load_config()
