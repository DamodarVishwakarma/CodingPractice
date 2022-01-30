class Bird:
    def intro(self):
        print("All birds can fly")

    def flight(self):
        print("some bird can fly or some can not  fly")


class Parrot(Bird):
    def flight(self):
        print("Parrot can also fly")


class Ostrich(Bird):
    def flight(self):
        print("ostrich can fly")


B = Bird()
P = Parrot()
O = Ostrich()
B.intro()
B.flight()
P.intro()
P.flight()
O.intro()
O.flight()
