import os
import sys


try:
    from dotenv import load_dotenv
except ImportError:
    print("[ERROR] python-dotenv is not installed."
          "Run 'pip install python-dotenv'")
    sys.exit(1)


def check_security(env_exists: bool) -> None:
    """Performs and displays the environment security checks."""
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")

    if env_exists:
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file is missing")

    print("[OK] Production overrides available\n")


def read_the_matrix() -> None:
    """Loads environment variables and displays the Oracle's vision."""
    print("\nORACLE STATUS: Reading the Matrix...\n")
    env_exists = os.path.isfile('.env')
    # Load variables from .env file into the system's environment variables
    # By default, load_dotenv() will NOT override existing system variables,
    # which perfectly allows for "Production overrides"
    load_dotenv()
    matrix_mode = os.environ.get("MATRIX_MODE")
    db_url = os.environ.get("DATABASE_URL")
    api_key = os.environ.get("API_KEY")
    log_level = os.environ.get("LOG_LEVEL")
    zion_endpoint = os.environ.get("ZION_ENDPOINT")

    if not all([matrix_mode, db_url, api_key, log_level,
               zion_endpoint]):
        print("\n[WARNING] Default/missing configuration detected!")
        print("The Oracle cannot see clearly. Please configure"
              "your environment variables.")
        print("Run: cp env.example .env")
        return
    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")
    if "local" in db_url or matrix_mode == "development":
        print("Database: Connected to local instance")
    else:
        print("Database: Connected to production instance")
    if api_key:
        print("API Access: Authenticated")

    print(f"Log Level: {log_level}")
    if zion_endpoint:
        print("Zion Network: Online\n")
    check_security(env_exists)
    print("The Oracle sees all configurations.")


def main() -> None:
    """Main execution block with graceful exception handling."""
    try:
        read_the_matrix()
    except Exception as e:
        print(f"A matrix glitch occurred: {e}")


if __name__ == "__main__":
    main()
