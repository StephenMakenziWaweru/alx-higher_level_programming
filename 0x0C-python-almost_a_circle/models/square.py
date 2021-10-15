#!/usr/bin/python3
"""Square class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """square constructor"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """Returns a string rep of this square"""
        return "[{}] ({}) {}/{} - {}"\
            .format(type(self).__name__, self.id, self.x, self.y,
                    self.height)

    @property
    def size(self):
        """This square size property"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """internal method for updating square"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Updates the square"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """returns a dictionary rep of this square"""
        return {"id": self.id, "size": self.size, "x": self.x,
                "y": self.y}
