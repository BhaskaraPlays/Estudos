class car:
    def __init__(self):
        self.color = 'red'
        self.make = 'mercedes'
pi= 3,14
class Elevator:
    def __init__(self, starting_floor):
        self.make = "The elevator company"
        self.floor = starting_floor

# To create the object

elevator = Elevator(1)
#print(elevator.make) # "The Elevator company"
#print(elevator.floor) # 1
class book:
    def __init__(self):
        self.make = 'cutchulo'
        self.caps = 6
        self.pages = 65
        self.autor = 'lovecraft'
booki = book()
#print(f'O livro {booki.make} possui {booki.caps} capitulos, {booki.pages} páginas e foi escrito por {booki.autor}')
class Square:
    def __init__(self):
        self.__height = 2
        self.__width = 2
    def set_side(self, new_side):
        self.__height = new_side
        self.__width = new_side
    def get_height(self):
        return self.__height
    @property
    def height(self):
        return self.__height
    @height.setter
    def set_height(self, h):
        if h >= 0:
            self.__height = h
        else:
            raise Exception ('value needs to be 0 or larger')
square = Square()
square.__height = 3