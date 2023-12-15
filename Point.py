import math

class Point:
    nb = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        Point.nb += 1

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    def __str__(self):
        return f"({self.__x},{self.__y})"

    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y

    def calculerdistance(self, p):
        return math.sqrt(math.pow((self.__x - p.__x), 2) + math.pow((self.__y - p.__y), 2))

    def calculermilieu(self, p):
        xM = (self.__x + p.__x) / 2
        yM = (self.__y + p.__y) / 2
        return Point(xM, yM)

    @staticmethod
    def calculerdistancestatique(p1, p2):
        return math.sqrt(math.pow((p1.x - p2.x), 2) + math.pow((p1.y - p2.y), 2))

    @staticmethod
    def calculermilieustatique(p1, p2):
        xM = (p1.x + p2.x) / 2
        yM = (p1.y + p2.y) / 2
        return Point(xM, yM)

class TroisPoints:
    def __init__(self, point1, point2, point3):
        self.__point1 = point1
        self.__point2 = point2
        self.__point3 = point3

    @property
    def point1(self):
        return self.__point1

    @point1.setter
    def point1(self, value):
        self.__point1 = value

    @property
    def point2(self):
        return self.__point2

    @point2.setter
    def point2(self, value):
        self.__point2 = value

    @property
    def point3(self):
        return self.__point3

    @point3.setter
    def point3(self, value):
        self.__point3 = value

    def sontalignes(self):
        ab = self.__point1.calculerdistance(self.__point2)
        ac = self.__point1.calculerdistance(self.__point3)
        bc = self.__point2.calculerdistance(self.__point3)
        return ab == ac + bc or ac == ab + bc or bc == ac + ab

    def estisocèle(self):
        ab = self.__point1.calculerdistance(self.__point2)
        ac = self.__point1.calculerdistance(self.__point3)
        bc = self.__point2.calculerdistance(self.__point3)
        return ab == ac or ab == bc or bc == ac

# Dans import math

class Point:
    nb = 0

    def __init__(self, abs, ord):
        self.__abs = abs
        self.__ord = ord
        Point.nb += 1

    @property
    def abs(self):
        return self.__abs

    @abs.setter
    def abs(self, value):
        self.__abs = value

    @property
    def ord(self):
        return self.__ord

    @ord.setter
    def ord(self, value):
        self.__ord = value

    def __str__(self):
        return f"({self.__abs},{self.__ord})"

    def __eq__(self, other):
        return self.__abs == other.__abs and self.__ord == other.__ord

    def calculerdistance(self, p):
        return math.sqrt(math.pow((self.__abs - p.__abs), 2) + math.pow((self.__ord - p.__ord), 2))

    def calculermilieu(self, p):
        xM = (self.__abs + p.__abs) / 2
        yM = (self.__ord + p.__ord) / 2
        return Point(xM, yM)

    @staticmethod
    def calculerdistancestatique(p1, p2):
        return math.sqrt(math.pow((p1.abs - p2.abs), 2) + math.pow((p1.ord - p2.ord), 2))

    @staticmethod
    def calculermilieustatique(p1, p2):
        xM = (p1.abs + p2.abs) / 2
        yM = (p1.ord + p2.ord) / 2
        return Point(xM, yM)

class TroisPoints:
    def __init__(self, point1, point2, point3):
        self.__point1 = point1
        self.__point2 = point2
        self.__point3 = point3

    @property
    def point1(self):
        return self.__point1

    @point1.setter
    def point1(self, value):
        self.__point1 = value

    @property
    def point2(self):
        return self.__point2

    @point2.setter
    def point2(self, value):
        self.__point2 = value

    @property
    def point3(self):
        return self.__point3

    @point3.setter
    def point3(self, value):
        self.__point3 = value

    def sontalignes(self):
        ab = self.__point1.calculerdistance(self.__point2)
        ac = self.__point1.calculerdistance(self.__point3)
        bc = self.__point2.calculerdistance(self.__point3)
        return ab == ac + bc or ac == ab + bc or bc == ac + ab

    def estisocèle(self):
        ab = self.__point1.calculerdistance(self.__point2)
        ac = self.__point1.calculerdistance(self.__point3)
        bc = self.__point2.calculerdistance(self.__point3)
        return ab == ac or ab == bc or bc == ac
