def is_number(number):
    try:
        float(number)
        return True
    except:
        return False


class Vector_2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector_2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        return self + other

    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + "]"


class Shape:
    color = ["black", "white", "red", "green", "blue", "cyan", "magenta", "yellow"] # myląca nazwa + jeśli to stała, to raczej nazwa wielkimi literami

    def __init__(self, name, *size):
        self.name = name
        self.spot = Vector_2D(0, 0)
        self.angle = 0
        self.size = [float(i) for i in size]
        self.border_color = "black"
        self.background_color = "white"

    def set_background_color(self, color):
        if color in Shape.color:
            self.background_color = color
        else:
            print("Color is not available") # lepiej sygnalizować błąd wyjątkiem

    def set_border_color(self, color):
        if color in Shape.color:
            self.border_color = color
        else:
            print("Color is not available")

    def move(self, x, y):
        if is_number(x) and is_number(y):   # jeśli x i y są już liczbami, to to sprawdzenie nie ma sensu
            self.spot += Vector_2D(x, y)    # a jeśli nie są, to tutaj mamy TypeError

    def rotate(self, degrees):
        if is_number(degrees):  # powinniśmy założyć, że parametry są odpowiedniego typu
            self.angle += degrees
            while self.angle > 360:
                self.angle -= 360
        else:
            print('Degrees must be a float')

    def scale(self, ratio):
        if is_number(ratio):
            if ratio != 0:
                self.size = [i * ratio for i in self.size]
            else:
                print("Ratio cant be 0!")
        else:
            print('Ratio must be a float')

    def __str__(self):
        return "name: {}, border color: {}, background color: {}, angle: {} degrees, spot: {}, size: {}".format(self.name, self.border_color,
                                                                                                                self.background_color, self.angle, self.spot, self.size)


class Circle(Shape):

    def __init__(self, name, *size):
        super().__init__(name, *size)
        if len(size) != 1:
            raise ValueError

    def __str__(self):
        return "Figure: circle, " + super().__str__()


class Square(Shape):

    def __init__(self, name, *size):
        super().__init__(name, *size)
        if len(size) != 1:
            raise ValueError    # przydałby się komunikat

    def __str__(self):
        return "Figure: square, " + super().__str__()


class Triangle(Shape):

    def __init__(self, name, *size):
        super().__init__(name, *size)
        if len(size) != 3:
            raise ValueError

        if self.size[0] + self.size[1] <= self.size[2] or self.size[1] + self.size[2] <= self.size[0] or self.size[0] + self.size[2] <= self.size[1]:
            raise ValueError

    def __str__(self):
        return "Figure: triangle, " + super().__str__()


class Rectangle(Shape):

    def __init__(self, name, *size):
        super().__init__(name, *size)
        if len(size) != 2:
            raise ValueError

    def __str__(self):
        return "Figure: rectangle, " + super().__str__()
