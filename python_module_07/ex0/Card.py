from abc import ABC, abstractmethod
from typing import Dict, Any


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        pass

    def get_card_info(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity,
            'type': self.__class__.__name__.replace('Card', '')
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
