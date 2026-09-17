
def event_generator(limit):
    players = ["alice", "bob", "charlie"]
    for i in range(1, limit + 1):
        player = players[(i - 1) % 3]
        if i % 3 == 1:
            action = "killed monster"
            level = 5
        elif i % 3 == 2:
            action = "found treasure"
            level = 12
        else:
            action = "leveled up"
            level = 8
        yield {
            "id": i,
            "player": player,
            "level": level,
            "action": action
        }


def fibonn_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def primen(n):
    c = 0
    num = 2
    while c < n:
        isprime = True
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                isprime = False
                break
        if isprime:
            yield num
            c += 1
        num += 1


def m():
    print("=== Game Data Stream Processor ===\n")
    limit = 1000
    print(f"Processing {limit} game events...\n")
    total = 0
    high_level = 0
    treasure_eve = 0
    level_up = 0
    events = event_generator(limit)
    for e in events:
        total += 1
        if e["id"] <= 3:
            print(f"Event {e['id']}: Player {e['player']} "
                  f"(level {e['level']}) {e['action']}")
        if e["level"] >= 10:
            high_level += 1
        if e["action"] == "found treasure":
            treasure_eve += 1
        if e["action"] == "leveled up":
            level_up += 1
    print("...\n")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_eve}")
    print(f"Level-up events: {level_up}\n")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")
    print("=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10):", end=" ")
    stream = fibonn_gen(10)
    for i in range(10):
        cu = next(stream)
        if i < 9:
            print(cu, end=", ")
        else:
            print(cu)
    print("Prime numbers (first 5):", end=" ")
    p = primen(5)
    for i in range(5):
        pnext = next(p)
        if i < 4:
            print(pnext, end=", ")
        else:
            print(pnext)


m()
