import math


class Shape:
    def __init__(self):
        pass

    def perimeter(self):
        raise NotImplementedError

    def area(self):
        raise NotImplementedError

    def copy(self):
        raise NotImplementedError


class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__()
        self.__a = a
        self.__b = b
        self.__c = c

    def perimeter(self):
        return self.__a + self.__b + self.__c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))

    def copy(self):
        return Triangle(self.__a, self.__b, self.__c)


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def area(self):
        return self.__width * self.__height

    def copy(self):
        return Rectangle(self.__width, self.__height)


class Trapeze(Shape):
    def __init__(self, a, b, c, d):
        super().__init__()
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d

    def perimeter(self):
        return self.__a + self.__b + self.__c + self.__d

    def area(self):
        h = math.sqrt(self.__c ** 2 - ((self.__b - self.__a) / 2) ** 2)
        return ((self.__a + self.__b) / 2) * h

    def copy(self):
        return Trapeze(self.__a, self.__b, self.__c, self.__d)


class Parallelogram(Shape):
    def __init__(self, base, side, height):
        super().__init__()
        self.__base = base
        self.__side = side
        self.__height = height

    def perimeter(self):
        return 2 * (self.__base + self.__side)

    def area(self):
        return self.__base * self.__height

    def copy(self):
        return Parallelogram(self.__base, self.__side, self.__height)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def perimeter(self):
        return 2 * math.pi * self.__radius

    def area(self):
        return math.pi * self.__radius ** 2

    def copy(self):
        return Circle(self.__radius)


def parse_input(file_path):
    figures = []
    with open(file_path, "r") as file:
        for line in file:
            parts = line.split()
            if parts:
                name = parts[0]
                parameters = list(map(float, parts[1:]))
                figures.append((name, parameters))
    return figures


def create_shape(name, params):
    if name == "Triangle":
        return Triangle(*params)
    elif name == "Rectangle":
        return Rectangle(*params)
    elif name == "Trapeze":
        return Trapeze(*params)
    elif name == "Parallelogram":
        return Parallelogram(*params)
    elif name == "Circle":
        return Circle(*params)
    return None


def find_largest_shapes(file_paths):
    max_area_shape = None
    max_perimeter_shape = None
    max_area = max_perimeter = float('-inf')

    for file_path in file_paths:
        figures = parse_input(file_path)
        for name, params in figures:
            shape = create_shape(name, params)
            if shape:
                area = shape.area()
                perimeter = shape.perimeter()
                if area > max_area:
                    max_area = area
                    max_area_shape = shape.copy()
                if perimeter > max_perimeter:
                    max_perimeter = perimeter
                    max_perimeter_shape = shape.copy()

    return max_area_shape, max_perimeter_shape


def main():
    input_files = ["input01.txt", "input02.txt", "input03.txt"]
    max_area_shape, max_perimeter_shape = find_largest_shapes(input_files)

    with open("output.txt", "w") as file:
        file.write(f"Largest Area: {max_area_shape.__class__.__name__} - Area: {max_area_shape.area():.2f}\n")
        file.write(
            f"Largest Perimeter: {max_perimeter_shape.__class__.__name__} - Perimeter: {max_perimeter_shape.perimeter():.2f}\n")
    print("Result saved to output.txt")


if __name__ == "__main__":
    main()
