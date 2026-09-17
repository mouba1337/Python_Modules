
import math


def cal_dist(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2
                     + (p2[2] - p1[2])**2)


def f():
    print("=== Game Coordinate System ===\n")
    origin = (0, 0, 0)
    po = (10, 20, 5)
    print(f"Position created: {po}")
    print(f"Distance between {origin} and {po}: {cal_dist(po, origin):.2f}\n")
    strr = "3,4,0"
    srr = "abc,def,ghi"
    try:
        print(f"Parsing coordinates: \"{strr}\"")
        ssp = strr.split(',')
        tsp = tuple(int(p) for p in ssp)
        print(f"Parsed position: {tsp}")
        print(f"Distance between {origin} and {tsp}: "
              f"{cal_dist(tsp, origin):.1f}\n")
        print(f"Parsing coordinates: \"{srr}\"")
        s = srr.split(',')
        ss = tuple(int(i) for i in s)
        print(ss)

    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}\n")
    print("Unpacking demonstration:")
    x, y, z = tsp
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


f()
