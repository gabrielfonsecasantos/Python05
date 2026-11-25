import os
import dotenv


def load_env_vars() -> None:
    dotenv.load_dotenv()

    print("ORACLE STATUS: Consulting the configuration...\n")
    missing_env_vars: list[str] = []

    matrix = os.getenv("MATRIX_MODE")
    if not matrix:
        missing_env_vars.append("MATRIX_MODE")
        matrix = "development"

    db = os.getenv("DATABASE_URL")
    if not db:
        missing_env_vars.append("DATABASE_URL")

    api_key = os.getenv("API_KEY")
    if not api_key:
        missing_env_vars.append("API_KEY")

    log_level = os.getenv("LOG_LEVEL")
    if not log_level:
        missing_env_vars.append("LOG_LEVEL")

    zion_endpoint = os.getenv("ZION_ENDPOINT")
    if not zion_endpoint:
        missing_env_vars.append("ZION_ENDPOINT")

    if len(missing_env_vars) > 0:
        print(f"The following configuration is missing from .env file: "
              f"{missing_env_vars}\n")

    print("Configuration loaded:")
    print(f"Mode: {matrix}")

    if matrix.lower() == "development":
        log_level = log_level if log_level else "Default: INFO"
        api_key = api_key if api_key else "Default: unauthenticated"
        zion_endpoint = zion_endpoint if zion_endpoint else "Default: Offline"
        db = db if db else "Default: Not Connected"
        print(f"Database: {db}.")
        print(f"API Access: {api_key}.")
        print(f"Log Level: {log_level}")
        print(f"Remote Network: {zion_endpoint}")
    elif matrix.lower() == "production":
        log_level = log_level if log_level else "Default: DEBUG"
        api_key = api_key if api_key else "Default: Authenticated"
        zion_endpoint = zion_endpoint if zion_endpoint else "Default: Online"
        db = db if db else "Default: Connected"
        print(f"Database: {db}.")
        print(f"API Access: {api_key}")
        print(f"Log Level: {log_level}")
        print(f"Remote Network: {zion_endpoint}")


if __name__ == "__main__":
    load_env_vars()
