from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Combine two spells into one that calls both with the same arguments."""
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Amplify spell power by multiplying the power before casting."""
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Cast a spell only if the condition evaluates to True."""
    def guarded_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return guarded_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    """Create a spell sequence that casts all provided spells in order."""
    def sequence_cast(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return sequence_cast


def main() -> None:
    """Demonstrates the use and efficiency of all spell modifier functions."""

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target}"

    def heal(target: str, power: int) -> str:
        return f"Heals {target}"

    def power_check(target: str, power: int) -> str:
        return str(power)

    def is_powerful_enough(target: str, power: int) -> bool:
        return power >= 50
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    res1, res2 = combined("Dragon", 50)
    print(f"Combined spell result: {res1}, {res2}\n")

    print("Testing power amplifier...")
    amplified = power_amplifier(power_check, 3)
    original_power = power_check("Target", 10)
    amplified_power = amplified("Target", 10)
    print(f"Original: {original_power}, Amplified: {amplified_power}")

    print("\nTesting conditional caster...")
    guarded_spell = conditional_caster(is_powerful_enough, fireball)
    print(f"Weak cast (20 power): {guarded_spell('Goblin', 20)}")
    print(f"Strong cast (60 power): {guarded_spell('Goblin', 60)}")

    print("\nTesting spell sequence...")
    seq = spell_sequence([fireball, heal, fireball])
    sequence_results = seq("Dark Knight", 100)
    for result in sequence_results:
        print(f"- {result}")


if __name__ == "__main__":
    main()
