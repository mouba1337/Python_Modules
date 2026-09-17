
def ps():
    print("=== Achievement Tracker System ===\n")
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer',
               'speed_demon', 'perfectionist'}
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}\n")
    unique = alice.union(bob, charlie)
    print("=== Achievement Analytics ===")
    print(f"All unique achievements:{unique}")
    print(f"Total unique achievements: {len(unique)}\n")
    common = alice & bob & charlie
    print(f"Common to all players: {common}")
    rare = (alice.difference(bob, charlie) | bob.difference(alice, charlie) |
            charlie.difference(bob, alice))
    print(f"Rare achievements (1 player): {rare}\n")
    abcommon = alice & bob
    au = alice.difference(bob)
    bu = bob.difference(alice)
    print(f"Alice vs Bob common: {abcommon}")
    print(f"Alice unique: {au}")
    print(f"Bob unique: {bu}")


ps()
