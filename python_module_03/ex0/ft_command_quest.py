
import sys


def sss():
    print("=== Command Quest ===")
    arg = sys.argv[1:]
    if not arg:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {len(arg)}")
        i = 1
        for g in arg:
            print(f"Argument {i}: {g}")
            i += 1
    print(f"Total arguments: {len(sys.argv)}")


sss()
