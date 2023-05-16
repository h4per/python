import math

class Figure:
    unit = "cm"

    def calculate_area():
        pass

    def info():
        pass

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, new_radius):
        self.__radius = new_radius

    def calculate_area(self):
        return round(math.pi * self.__radius ** 2)
    
    def info(self):
        print(f"Радиус круга: {self.__radius}\nПлощадь круга: {self.calculate_area()}{self.unit}\n")
    
crug = Circle(20)
# crug.info()


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return round(0.5 * self.__side_a * self.__side_b)
    
    def info(self):
        print(f"\nСторона а: {self.__side_a}{self.unit}\nСторона b: {self.__side_b}{self.unit}\nПлощадь прямоугольного треугольника: {self.calculate_area()}{self.unit}")


triugolnik = RightTriangle(5,4)
# triugolnik.info()


crug1 = Circle(4)
crug2= Circle(2)
triugolnik1 = RightTriangle(3,6)
triugolnik2 = RightTriangle(5,9)
triugolnik3 = RightTriangle(8,10)
figures = [crug1, crug2, triugolnik1, triugolnik2, triugolnik3]
# for figure in figures:
#     figure.info()
