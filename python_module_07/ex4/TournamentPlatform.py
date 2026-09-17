from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.registered_cards: dict[str, TournamentCard] = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.registered_cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if (card1_id not in self.registered_cards or
                card2_id not in self.registered_cards):
            return {"error": "Cards not found"}

        card1 = self.registered_cards[card1_id]
        card2 = self.registered_cards[card2_id]

        card1.update_wins(1)
        card2.update_losses(1)
        self.matches_played += 1

        return {
            'winner': card1_id,
            'loser': card2_id,
            'winner_rating': card1.calculate_rating(),
            'loser_rating': card2.calculate_rating()
        }

    def get_leaderboard(self) -> list:
        sorted_cards = (sorted(self.registered_cards.values(),
                               key=lambda c: c.calculate_rating(),
                               reverse=True))
        return [
            f"{card.name} Rating: {card.calculate_rating()} "
            f"({card.wins}-{card.losses})"
            for card in sorted_cards
        ]

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.registered_cards)
        avg_rating = (
            sum(c.calculate_rating() for c in self.registered_cards.values())
            / total_cards if total_cards > 0 else 0
        )

        return {
            'total_cards': total_cards,
            'matches_played': self.matches_played,
            'avg_rating': int(avg_rating),
            'platform_status': 'active'
        }
