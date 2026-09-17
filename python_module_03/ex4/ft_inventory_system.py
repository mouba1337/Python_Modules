
def inv():
    print("=== Player Inventory System ===\n")
    print("=== Alice's Inventory ===")
    al = {
        "sword": {"category": "weapon", "rarity": "rare",
                  "item": 1, "gold": 500},
        "potion": {"category": "consumable", "rarity": "common",
                   "item": 5, "gold": 50},
        "shield": {"category": "armor", "rarity": "uncommon",
                   "item": 1, "gold": 200}
    }
    asword = al['sword']
    apotion = al['potion']
    ashield = al['shield']
    swgold = asword['item'] * asword['gold']
    shgold = ashield['item'] * ashield['gold']
    pgold = apotion['item'] * apotion['gold']
    for i, j in al.items():
        print(f"{i} ({j['category']}, {j['rarity']}): {j['item']}x @ "
              f"{j['gold']} gold each = {j['item'] * j['gold']} gold")
    print(f"\nInventory value: {swgold + shgold + pgold} gold")
    print("Item count: "
          f"{asword.get('item') + apotion.get('item') + ashield.get('item')}"
          " items")
    print(f"Categories: {asword['category']}({asword['item']}), "
          f"{apotion['category']} ({apotion['item']}), "
          f"{ashield['category']}({ashield['item']})\n")
    apotion.update({"item": 3})
    bob = {"potion": {}, "magic_ring": {"rarity": "rare"}}
    bob["potion"].update({"item": 2})
    print("=== Transaction: Alice gives Bob 2 potions ===")
    print("Transaction successful!\n")
    print("=== Updated Inventories ===")
    print(f"Alice potions: {apotion['item']}")
    print(f"Bob potions: {bob['potion']['item']}\n")
    print("=== Inventory Analytics ===")
    print(f"Most valuable player: Alice ("
          f"{swgold + shgold + apotion['item'] * apotion['gold']} gold)")
    print("Most items: Alice ("
          f"{ashield['item'] + asword['item'] + apotion['item']} items)")
    rarest_alice = [i for i, j in al.items() if j.get("rarity") == "rare"]
    rarest_bob = [i for i, j in bob.items() if j.get("rarity") == "rare"]
    rarest = rarest_alice + rarest_bob
    print("Rarest items:", end=" ")
    print(*rarest, sep=", ")


inv()
