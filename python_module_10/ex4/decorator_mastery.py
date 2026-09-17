import time
import functools
import inspect
from collections.abc import Callable
from typing import Any


def spell_timer(func: Callable) -> Callable:
    """Decorator that measures and prints function execution time."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")

        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        duration = end_time - start_time
        print(f"Spell completed in {duration:.3f} seconds")

        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    """Decorator factory that validates the power argument of a spell."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:

            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            power_val = bound_args.arguments.get('power')
            if power_val is None and bound_args.arguments:
                power_val = list(bound_args.arguments.values())[0]

            if isinstance(power_val, int) and power_val >= min_power:
                return func(*args, **kwargs)

            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Decorator that automatically retries a failed function."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print("Spell failed, retrying... "
                              f"(attempt {attempt}/{max_attempts})")

            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    """
    A guild class demonstrating static methods and decorated instance methods.
    """

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """
        Validates if a name is at least 3 chars and
        contains only letters/spaces.
        """
        if len(name) < 3:
            return False
        return all(char.isalpha() or char.isspace() for char in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Instance method demonstrating decorator integration."""
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    """Demonstrate the decorator mastery exactly as requested."""

    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.101)
        return "Fireball cast!"

    print(f"Result: {fireball()}")
    print("\nTesting retrying spell")

    @retry_spell(max_attempts=3)
    def fail_spell() -> str:
        raise ValueError("Fizzled!")

    @retry_spell(max_attempts=3)
    def waagh_spell() -> str:
        return "Waaaaaaagh spelled !"

    print(fail_spell())
    print(waagh_spell())

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("Jo"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
