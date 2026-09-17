import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce spell powers using functools.reduce and operator module."""
    if not spells:
        return 0
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")

    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """
    Create specialized versions of a base enchantment using functools.partial.
    """
    return {
        "fire": functools.partial(base_enchantment, 50, "Fire"),
        "water": functools.partial(base_enchantment, 50, "Water"),
        "earth": functools.partial(base_enchantment, 50, "Earth")
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number using a memoization cache."""
    if n < 0:
        raise ValueError("Fibonacci sequence is not "
                         "defined for negative numbers.")
    if n in (0, 1):
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """Create a single dispatch system to handle different spell types."""

    @functools.singledispatch
    def dispatcher(arg: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @dispatcher.register(str)
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @dispatcher.register(list)
    def _(arg: list) -> str:
        return f"Multi-cast: {len(arg)} spells"

    return dispatcher


def main() -> None:
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch([1, 2, 3]))
    print(dispatch(3.14))


if __name__ == "__main__":
    main()
