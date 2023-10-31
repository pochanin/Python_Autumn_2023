class Shape:
    def __init__(self):
        self.colour = ''
        self.square = 0

    def set_colour(self, colour):
        self.colour = colour

    def get_colour(self):
        print('Цвет объекта: ', self.colour)

    def set_square(self, square):
        self.square = square

    def get_square(self):
        print('Площадь объекта: ', self.square)

# создание объекта
shape = Shape()
# установка цвета
shape.set_colour("Красный")
# получение цвета
shape.get_colour()
# Задание площади
shape.set_square(10)
# получение площади
shape.get_square()