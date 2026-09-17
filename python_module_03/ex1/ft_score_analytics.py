
import sys


def s():
    print("=== Player Score Analytics ===")
    if len(sys.argv) < 2:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
        return
    try:
        scores = [int(arg) for arg in sys.argv[1:]]
        print(f"Scores processed: {scores}")
        print(f"total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low scores: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
    except ValueError:
        print("Error: All scores must be integers.")


s()
