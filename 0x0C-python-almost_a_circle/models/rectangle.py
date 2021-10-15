#!/usr/bin/python3
"""Rectangle class module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def validate(self, name, value):
        """validates all values"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if (name == "width" or name == "height") and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif (name == "x" or name == "y") and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def x(self):
        """rectangle's x pos"""
        return self.__x

    @x.setter
    def x(self, value):
        self.validate("x", value)
        self.__x = value

    @property
    def y(self):
        """rectangle's y pos"""
        return self.__y

    @y.setter
    def y(self, value):
        self.validate("y", value)
        self.__y = value

    @property
    def width(self):
        """rectangle's width"""
        return self.__width

    @width.setter
    def width(self, value):
        self.validate("width", value)
        self.__width = value

    @property
    def height(self):
        """rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.validate("height", value)
        self.__height = value

    def area(self):
        """returns area of this rectangle"""
        return self.width * self.height

    def display(self):
        """Prints rectangle instance with the character #"""
        rec_s = "\n" * self.y + (" " * self.x + "#" * self.width +
                                 "\n") * self.height
        print(rec_s, end="")

    def __str__(self):
        """returns a string rep of this rectangle"""
        return "[{}] ({}) {}/{} - {}/{}"\
            .format(type(self).__name__, self.id, self.x, self.y,
                    self.width, self.height)

    def __updArgsKwarg(self, id=None, width=None, height=None, x=None, y=None):
        """Internal method for updating the square"""
        args = locals()
        for k in args.keys():
            if args[k] is not None and k != "self" and k == "id":
                self.__dict__[k] = args[k]
            elif args[k] is not None and k != "self":
                self.__dict__["_" + type(self).__name__ + "__" + k] = args[k]

    def update(self, *args, **kwargs):
        """Updates the square"""
        if args:
            self.__updArgsKwarg(*args)
        elif kwargs:
            self.__updArgsKwarg(**kwargs)

    def to_dictionary(self):
        """returns a dictionary rep of this rectangle"""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
