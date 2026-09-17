def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort magical artifacts by power level (descending)."""
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Filter mages to only keep those with power >= min_power."""
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Add '*' prefix and '*' suffix to spell names."""
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """Calculate max, min, and average power levels of mages."""
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    max_p = max(mages, key=lambda m: m['power'])['power']
    min_p = min(mages, key=lambda m: m['power'])['power']

    total_power = sum(map(lambda m: m['power'], mages))
    avg_p = round(total_power / len(mages), 2)

    return {
        'max_power': max_p,
        'min_power': min_p,
        'avg_power': avg_p
    }


def main() -> None:
    """Demonstrate the lambda spells."""

    print("Testing artifact sorter...")
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Basic Wand', 'power': 15, 'type': 'weapon'}
    ]
    sorted_arts = artifact_sorter(artifacts)
    print(f"{sorted_arts[0]['name']} ({sorted_arts[0]['power']} power) "
          f"comes before {sorted_arts[1]['name']}"
          f" ({sorted_arts[1]['power']} power)\n")

    print("Testing spell transformer...")
    spells = ['fireball', 'heal', 'shield']
    transformed = spell_transformer(spells)
    for spell in transformed:
        print(spell, end=" ")


if __name__ == "__main__":
    main()
