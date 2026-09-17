from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("=== DataDeck Deck Builder ===")
    print("Building deck with different card types...")

    deck = Deck()

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    lightning = SpellCard("Lightning Bolt", 3, "Common",
                          "Deal 3 damage to target")
    mana_crystal = ArtifactCard("Mana Crystal", 2, "Rare", 3,
                                "Permanent: +1 mana per turn")

    deck.add_card(dragon)
    deck.add_card(lightning)
    deck.add_card(mana_crystal)

    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:")

    cards_to_play = [lightning, mana_crystal, dragon]

    for card in cards_to_play:
        card_type = card.__class__.__name__.replace('Card', '')
        print(f"Drew: {card.name} ({card_type})")
        print(f"Play result: {card.play({})}")

    print("\nPolymorphism in action: Same interface, "
          "different card behaviors!")


if __name__ == "__main__":
    main()
