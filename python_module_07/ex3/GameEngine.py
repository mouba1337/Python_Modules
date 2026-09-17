from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        self.turns_simulated += 1
        self.cards_created += 3

        turn_result = self.strategy.execute_turn([], [])
        self.total_damage += turn_result.get('damage_dealt', 0)

        return turn_result

    def get_engine_status(self) -> dict:
        strategy_name = (self.strategy.get_strategy_name()
                         if self.strategy else "None")
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': strategy_name,
            'total_damage': self.total_damage,
            'cards_created': self.cards_created
        }
