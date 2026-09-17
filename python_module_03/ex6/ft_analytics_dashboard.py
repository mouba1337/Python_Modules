
def main():
    print("=== Game Analytics Dashboard ===")
    game_data = [
        {"name": "alice", "score": 2300, "role": "tank",
         "achievements": ["first_kill", "level_10", "collector"],
         "region": "north"},
        {"name": "bob", "score": 1800, "role": "healer",
         "achievements": ["level_10"], "region": "east"},
        {"name": "charlie", "score": 2150, "role": "dps",
         "achievements": ["level_10", "boss_slayer"], "region": "central"},
        {"name": "diana", "score": 2500, "role": "tank",
         "achievements": ["speed_demon", "collector"], "region": "central"}
    ]
    scores = [2300, 1800, 2150, 1900, 2800, 1500]
    print("\n=== List Comprehension Examples ===")
    high_scorers = [p["name"] for p in game_data if p["score"] > 2000]
    print(f"High scorers (>2000): {high_scorers}")
    doubled = [i["score"] * 2 for i in game_data]
    print(f"Scores doubled: {doubled}")
    active_players = [p["name"] for p in game_data]
    print(f"Active players: {active_players}\n")
    print("=== Dict Comprehension Examples ===")
    player_scores = {j["name"]: j["score"] for j in game_data}
    print(f"Player scores: {player_scores}")
    score_catego = {
        "high": sum(1 for s in scores if s > 2000),
        "medium": sum(2 for s in scores if 1800 <= s <= 2000),
        "low": sum(1 for s in scores if s < 2000)
    }
    print(f"Score categories: {score_catego}")
    achiev_counter = {f["name"]: len(f["achievements"]) for f in game_data}
    print(f"Achievement counts: {achiev_counter}\n")
    print("=== Set Comprehension Examples ===")
    unique_play = {u["name"] for u in game_data}
    print(f"Unique players: {unique_play}")
    unique_roles = {r["role"] for r in game_data}
    print(f"Unique roles: {unique_roles}")
    regions = {v["region"] for v in game_data}
    print(f"Active regions: {regions}\n")
    print("=== Combined Analysis ===")
    print(f"Total players: {len(game_data)}")
    unique_ach = {a for i in game_data for a in i["achievements"]}
    print(f"Total unique achievements: {len(unique_ach)}")
    average_score = sum(scores) / len(scores)
    print(f"Average score: {average_score}")
    max_score = max(p["score"] for p in game_data)
    top_player = [p["name"] for p in game_data if p["score"] == max_score]
    print(f"Top performer: {top_player[0]} ({max_score} points)")


main()
