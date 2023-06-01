#!/usr/bin/python3
""" Class: Square """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Describes a Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ Init method """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y}\
 - {self.width}"
