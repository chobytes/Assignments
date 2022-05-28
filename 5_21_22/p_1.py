from math import pi

class GeometricObject:
    def __init__(self, color: str = "Green", filled: bool = "False") -> None:
        self.__color = color
        self.__filled = filled
    
    def getColor(self) -> str:
        return self.__color

    def setColor(self, color: str) -> None:
        self.__color = color
    
    def isFilled(self) -> bool:
        return self.__filled

    def setfilled(self, filled: bool) -> None:
        self.__filled = filled

    def __str__(self):
        return f"color: {self.__color} and filled: {self.__filled}"
    
       
class Circle(GeometricObject):
    def __init__(self, radius: float) -> None:
        super().__init__()
        self.__radius = radius

    def getRadius(self) -> float:
        return self.__radius

    def setRadius(self, radius: float) -> None:
        self.__radius = radius

    def getArea(self) -> float:
        return pi * pow(self.__radius,2)

    def getPerimeter(self) -> float:
        return 2 * pi * self.__radius

    def getDiameter(self) -> float:
        return 2 * self.__radius

    def printCircle(self) -> None:
        print(self)
    
    def __str__(self) -> str:
        return f"{super().__str__()} radius: {self.__radius}"
    
class Rectangle(GeometricObject):
    def __init__(self, width, height) -> None:
        super().__init__()
        self.__width = width
        self.__height = height

    def getWidth(self) -> float:
        return self.__width

    def setWidth(self, width: float) -> None:
        self.__width = width

    def getHeight(self) -> float:
        return self.__height

    def setHeight(self, height: float) -> None:
        self.__height = height
    
    def getArea(self) -> float:
        return self.__width * self.__height

    def getPerimeter(self) -> float:
        return 2 * (self.__width + self.__height)

    def __str__(self) -> str:
        return f"{super().__str__()} width: {self.__width} height: {self.__height}"

