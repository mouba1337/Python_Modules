import sys
import os
import site


def is_in_virtual_environment() -> bool:
    return (hasattr(sys, 'base_prefix') and
            sys.base_prefix != sys.prefix)


def display_outside_matrix() -> None:
    print("\nMATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")
    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("\nTo enter the construct, run:")
    print("  python -m venv matrix_env")
    print("  source matrix_env/bin/activate  # On Unix")
    print("  matrix_env\\Scripts\\activate   # On Windows")
    print("\nThen run this program again.")


def display_inside_construct() -> None:
    env_path = sys.prefix
    env_name = os.path.basename(env_path)
    print("\nMATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {env_name}")
    print(f"Environment Path: {env_path}")
    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the "
          "global system.")

    try:
        package_path = site.getsitepackages()[0]
    except (AttributeError, IndexError):
        package_path = os.path.join(
            env_path, 'lib',
            f'python{sys.version_info.major}.{sys.version_info.minor}',
            'site-packages'
        )

    print(f"\nPackage installation path:\n  {package_path}")


def main() -> None:
    try:
        if is_in_virtual_environment():
            display_inside_construct()
        else:
            display_outside_matrix()
    except Exception as e:
        print("A matrix glitch occurred during"
              f"environment detection: {e}")


if __name__ == "__main__":
    main()
