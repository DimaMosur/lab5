from enum import Enum
from math import sqrt


class Colour(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __del__(self):
        print(f"Point ({self.x}, {self.y}) has been deleted")

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def distance_to(self, other_point):
        return sqrt((self.x-other_point.x) ** 2 + (self.y-other_point.y) ** 2)


class Polynom:
    def __init__(self, points, colour):
        self.points = points
        self.colour = colour

    def __del__(self):
        print("Polynom has been deleted")

    def perimeter(self):
        if len(self.points) < 2:
            return 0
        perimeter = 0
        for i in range(len(self.points)):
            j = (i + 1) % len(self.points)
            perimeter += self.points[i].distance_to(self.points[j])
        return perimeter

    def longest_diagonal(self):
        max_distance = 0
        for i in range(len(self.points)):
            for j in range(i + 1, len(self.points)):
                distance = self.points[i].distance_to(self.points[j])
                if distance > max_distance:
                    max_distance = distance
        return max_distance

    def sort_points_by_x(self):
        self.points.sort(key=lambda p: p.x)

    def sort_points_by_y(self):
        self.points.sort(key=lambda p: p.y)

    def display_info(self):
        print("Polynom points:", self.points)
        print("Colour:", self.colour.name)
        print("Perimeter:", self.perimeter())
        print("Longest diagonal:", self.longest_diagonal())


def main():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    p3 = Point(6, 0)
    p4 = Point(3, -4)

    polynom = Polynom([p1, p2, p3, p4], Colour.BLUE)

    polynom.display_info()

    print("\nSorting points by x:")
    polynom.sort_points_by_x()
    polynom.display_info()

    print("\nSorting points by y:")
    polynom.sort_points_by_y()
    polynom.display_info()


main()
