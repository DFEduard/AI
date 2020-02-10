# File: Task_1.py
# Description: Task_1 class file
# Author: F. Eduard Decu
# Date: September 2019

from Temperature import Temp

class Task1():
    def __init__(self):
        pass

    def run(self):
        print("############### Exercise 1 ################")
        print("Welcome to temperature converter")
        print("From Celsius to Fahrenheit type 1")
        print("From Fahrenheit to Celsius type 2")
        userInput = int(input("Selected conversion: "))
        tempScales = ("C", "F")

        if userInput == 1:
            scale = tempScales[0]
        elif userInput == 2:
            scale = tempScales[1]

        tempValue = input("Temp in {0}: ".format(scale))
        temp = Temp(tempValue, scale)
        print(str(temp) + " = " + str(temp.convert))