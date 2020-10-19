from vectors import Vector, Point

def main():
    v1 = Vector(1,1,1)
    point1 = Point(1,1,1)
    print(point1.add(v1.multiply(5)))
    return 0

main()