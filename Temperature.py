# File: Temperature.py
# Description: Temperature class file
# Author: F. Eduard Decu
# Date: September 2019


class Temp:
    def __init__(self, temp, scale):
        self.__temp = temp
        self.__scale = scale

    """
    Read-only properties
    """
    @property
    def temp(self):
        return self.__temp
    @property
    def scale(self):
        return self.__scale

    @property
    def convert(self):
        if self.scale == "C":
            f = (float(self.temp) * 1.8 ) + 32
            return "{0:.2f}{1}".format(f," F")
        elif self.scale == "F":
            c = (float(self.temp) - 32)/1.8
            return "{0:.2f}{1}".format(c," C")

    def __str__(self):
        """
        :return: string representation of this class
        """
        s = "{0:.2f}{1}".format(float(self.temp), str(" " + self.scale))
        return s

