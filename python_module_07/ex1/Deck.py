import random
from ex0.Card import Card


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        if isinstance(card, Card):
            self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for i, card in enumerate(self.cards):
            if card.name == card_name:
                self.cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if self.cards:
            return self.cards.pop()
        return None

    def get_deck_stats(self) -> dict:
        creatures = sum(1 for c in self.cards
                        if c.__class__.__name__ == 'CreatureCard')
        spells = sum(1 for c in self.cards
                     if c.__class__.__name__ == 'SpellCard')
        artifacts = sum(1 for c in self.cards
                        if c.__class__.__name__ == 'ArtifactCard')
        total = len(self.cards)
        avg_cost = (sum(c.cost for c in self.cards) / total
                    if total > 0 else 0.0)

        return {
            'total_cards': total,
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts,
            'avg_cost': round(avg_cost, 2)
        }
