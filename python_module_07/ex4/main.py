from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===")
    print("Registering Tournament Cards...")

    platform = TournamentPlatform()

    dragon = TournamentCard("dragon_001",
                            "Fire Dragon", 5, "Legendary", 1200)
    wizard = TournamentCard("wizard_001",
                            "Ice Wizard", 4, "Epic", 1150)

    platform.register_card(dragon)
    platform.register_card(wizard)

    for card in [dragon, wizard]:
        stats = card.get_tournament_stats()
        print(f"{card.name} (ID: {stats['id']}):")
        print(f"Interfaces: [{', '.join(stats['interfaces'])}]")
        print(f"Rating: {stats['rating']}")
        print(f"Record: {stats['record']}")

    print("\nCreating tournament match...")
    match_result = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {match_result}")

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, entry in enumerate(leaderboard, 1):
        parts = entry.split(' Rating: ')
        print(f"{i}. {parts[0]}")
        print(f"Rating: {parts[1]}")

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
