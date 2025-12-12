from Circle import Circle
from Rectangle import Rectangle
from Square import Square

if __name__ == "__main__":
    shapes = [
        Circle(0, 0, 8, "Circle_1"),
        Circle(5, 5, 3, "Circle_2"),
        Rectangle(20, 25, "Rectangle_1"),
        Rectangle(40, 60, "Rectangle_2"),
        Square(20, "Square")
    ]

    print("--- Polymorphism check ---")
    for s in shapes:
        print(f"{s.name} Area = {s.area}")

    c1 = shapes[0]
    print("\n--- Getter/setter check")
    print(f"{c1.name} Current: {c1.radius} {c1.area}")
    c1.radius *= 2
    print(f"{c1.name} Doubled: {c1.radius} {c1.area}")

    r1 = shapes[2]
    print(f"{r1.name} Current: {r1.length} {r1.width} {r1.area}")
    r1.length *= 2
    r1.width *= 2
    print(f"{r1.name} Doubled: {r1.length} {r1.width} {r1.area}")

    sq = shapes[4]
    print(f"{sq.name} Current: {sq.side} {sq.area}")
    sq.side *= 2
    print(f"{sq.name} Doubled: {sq.side} {sq.area}")