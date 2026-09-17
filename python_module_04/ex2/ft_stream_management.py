
import sys


def m():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    id_ar = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")
    print(f"\n[STANDARD] Archive status from {id_ar}:  {status}",
          file=sys.stdout)
    print("[ALERT] System diagnostic: Communication channels verified",
          file=sys.stderr)
    print("{[}STANDARD{]} Data transmission complete", file=sys.stdout)
    print()
    print("\nThree-channel communication test successful.", file=sys.stdout)


m()
