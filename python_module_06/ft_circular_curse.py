from alchemy.grimoire.validator import validate_ingredients
from alchemy.grimoire.spellbook import record_spell

print("\n===Circular Curse Breaking ===\n")
print("Testing ingredient validation:")
print(f'validate_ingredients("fire air"): {validate_ingredients("fire air")}')
print(f'validate_ingredients("dragon scales"): {validate_ingredients("dragon scales")}\n')

print("Testing spell recording with validation:")
print(f'record_spell("Fireball", "fire air"): {record_spell("Fireball", "fire air")}')
print(f'record_spell("Dark Magic", "shadow"): {record_spell("Dark Magic", "shadow")}\n')

print("Testing late import technique:")
print(f'record_spell("Lightning", "air"): {record_spell("Lightning", "air")}')

print("\nCircular dependency curse avoided using late imports!\nAll spells processed safely!")