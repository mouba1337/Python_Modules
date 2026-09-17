from .CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    def create_creature(self,
                        name_or_power: str | int | None = None) -> Card:
        if name_or_power == "dragon":
            return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        return CreatureCard("Goblin Warrior", 2, "Common", 2, 1)

    def create_spell(self,
                     name_or_power: str | int | None = None) -> Card:
        if name_or_power == "fireball":
            return SpellCard("Fireball", 4, "Rare", "Deal 5 damage")
        return SpellCard("Lightning Bolt", 3, "Common", "Deal 3 damage")

    def create_artifact(self,
                        name_or_power: str | int | None = None) -> Card:
        return ArtifactCard("Mana Ring", 2,
                            "Uncommon", 5, "Permanent: +1 mana")

    def create_themed_deck(self, size: int) -> dict:
        return {'theme': 'Fantasy', 'size': size}

    def get_supported_types(self) -> dict:
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }
