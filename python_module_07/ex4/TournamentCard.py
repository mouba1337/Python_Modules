from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, card_id: str, name: str, cost: int,
                 rarity: str, base_rating: int = 1200):
        super().__init__(name, cost, rarity)
        self.card_id = card_id
        self.rating = base_rating
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Entered tournament arena'
        }

    def attack(self, target: str) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'action': 'Tournament strike'
        }

    def defend(self, incoming_damage: int) -> dict:
        return {
            'defender': self.name,
            'status': 'Defending in tournament'
        }

    def get_combat_stats(self) -> dict:
        return {'tournament_ready': True}

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += (wins * 16)

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= (losses * 16)

    def get_rank_info(self) -> dict:
        return {
            'rating': self.rating,
            'record': f"{self.wins}-{self.losses}"
        }

    def get_tournament_stats(self) -> dict:
        interfaces = [cls.__name__ for cls in self.__class__.__mro__
                      if cls.__name__ in ['Card', 'Combatable', 'Rankable']]
        interfaces.reverse()

        return {
            'id': self.card_id,
            'interfaces': interfaces,
            'rating': self.rating,
            'record': f"{self.wins}-{self.losses}"
        }
