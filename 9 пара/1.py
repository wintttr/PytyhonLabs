import math


def distance(d1, d2):
    return math.sqrt((d1[0] - d2[0]) ** 2 + (d1[1] - d2[1]) ** 2)


def rotate108(vec):
    angle = 108 * math.pi / 180
    x = vec[0] * math.cos(angle) + vec[1] * math.sin(angle)
    y = vec[0] * math.sin(angle) + vec[1] * math.cos(angle)
    return (x, y)


# v1 - v2, vi - двумерные векторы
def minus(v1, v2):
    return (v1[0] - v2[0], v1[1] - v2[1])


def plus(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])


class figure:
    def __init__(self, name):
        self.id = name

    def get_id(self):
        return self.id

    def get_edges(self):
        pass

    def get_square(self):
        pass


class triangle(figure):
    def __init__(self, name, d1, d2, d3):
        super().__init__(name)
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3

    def get_square(self):
        p1 = distance(self.d1, self.d2)
        p2 = distance(self.d2, self.d3)
        p3 = distance(self.d1, self.d3)
        p = (p1 + p2 + p3) / 2
        return math.sqrt(p * (p - p1) * (p - p2) * (p - p3))

    def get_edges(self):
        return [(self.d1, self.d2), (self.d2, self.d3), (self.d1, self.d3)]


class pentagon(figure):
    def __init__(self, name, centre, d):
        super().__init__(name)
        self.d = d
        self.R = distance(centre, d)
        self.C = centre

    def get_square(self):
        return 5 / 2 * self.R ** 2 * math.sin(2 * math.pi / 5)

    def get_edges(self):
        vect = minus(self.d, self.C)
        d1 = self.d
        vect = rotate108(vect)
        d2 = plus(self.C, vect)
        vect = rotate108(vect)
        d3 = plus(self.C, vect)
        vect = rotate108(vect)
        d4 = plus(self.C, vect)
        vect = rotate108(vect)
        d5 = plus(self.C, vect)
        return [(d1, d2), (d2, d3), (d3, d4), (d4, d5), (d5, d1)]


def compare(t1, t2):
    if (t1.get_square() > t2.get_square()):
        print("{} > {}".format(t1.get_id(), t2.get_id()))
    elif (t1.get_square() < t2.get_square()):
        print("{} < {}".format(t1.get_id(), t2.get_id()))
    else:
        print("{} = {}")


def intersect(e1, e2):
    ((x1, y1), (x2, y2)) = e1
    ((x3, y3), (x4, y4)) = e2

    de = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if (de == 0):
        return False

    Px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / de
    Py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / de

    if (Px > x1 and Px < x2 or Px < x1 and Px > x2):
        pass
    else:
        return False

    if (Px > x3 and Px < x4 or Px < x3 and Px > x4):
        pass
    else:
        return False

    if (Py > y1 and Py < y2 or Py < y1 and Py > y2):
        pass
    else:
        return False

    if (Py > y3 and Py < y4 or Py < y3 and Py > y4):
        pass
    else:
        return False

    return True


def isIntersect(t1, t2):
    t1_edges = t1.get_edges()
    t2_edges = t2.get_edges()

    if(len(t1_edges) == 0 or len(t2_edges) == 0):
        raise Exception()

    for i in t1_edges:
        for j in t2_edges:
            if (intersect(i, j)):
                return True
    return False


if __name__ == "__main__":
    try:
        t = triangle("triangle1", (1, 1), (4, 6), (6, 1))
        p = pentagon("pentagon1", (12, 7), (9, 4))

        print("Тест1")
        compare(t, p)
        print("Верный ответ - t1 < t2")
        if isIntersect(t, p):
            print("Пересекаются (ошибка)")
        else:
            print("Не пересекаются (всё норм)")

        print("\nТест2")
        p2 = pentagon("pentagon2", (6, 4), (4, 3))

        compare(t, p2)
        print("Верный ответ - t1 > t2")
        if isIntersect(t, p2):
            print("Пересекаются (всё норм)")
        else:
            print("Не пересекаются (ошибка)")
    except Exception:
        print("Ошибка! Пустой объект.")