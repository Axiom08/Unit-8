<<<<<<< HEAD
# Point class goes here
import math
class Point:
    # constructor
    def __init__(self, x_val:int, y_val:int):
        self.x = x_val
        self.y = y_val
        

    def distance(self, second_point):
        leg_a = self.x - second_point.x
        leg_b = self.y - second_point.y
        distance = math.sqrt(leg_a**2 + leg_b**2)
        return distance


def main():
    origin = Point(0, 0)
    c = Point(-3, 4)
    print(f'The origin is ({origin.x}, {origin.y})')
    print(f'The distance between {(origin.x, origin.y)} and {(c.x, c.y)} is {origin.distance(c)}')


if __name__ == '__main__':
    main()
=======
>>>>>>> 28598b6f35b9a5484f5879093dd0ef605c03c726
