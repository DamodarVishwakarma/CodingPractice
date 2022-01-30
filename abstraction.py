from abc import ABC


class Polygon(ABC):
    def sides(self):
        pass


class Tringle(Polygon):
    def sides(self):
        print("Tringle has 3 sides")


class Pentagon(Polygon):
    def sides(self):
        print("pentagon has 5 sides")


class Hexagon(Polygon):
    def sides(self):
        print("hexagon has 6 sides")


T = Tringle()
T.sides()
P = Pentagon
P.sides(4)
H = Hexagon()
H.sides()
