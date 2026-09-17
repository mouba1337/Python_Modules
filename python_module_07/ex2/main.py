from ex2.EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===")
    print("EliteCard capabilities:")
    print("Card: ['play', 'get_card_info', 'is_playable']")
    print("Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n")

    arcane_warrior = EliteCard(
        name="Arcane Warrior",
        cost=6,
        rarity="Epic",
        attack_power=5,
        defense=3,
        mana_pool=4
    )

    print("Playing Arcane Warrior (Elite Card):")

    print("Combat phase:")
    print(f"Attack result: {arcane_warrior.attack('Enemy')}")
    print(f"Defense result: {arcane_warrior.defend(5)}\n")

    print("Magic phase:")
    spell_result = arcane_warrior.cast_spell('Fireball', ['Enemy1', 'Enemy2'])
    print(f"Spell cast: {spell_result}")
    print(f"Mana channel: {arcane_warrior.channel_mana(3)}\n")

    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
