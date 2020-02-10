# File: AI Week 1.py
# Description: Temperature class file
# Author: F. Eduard Decu
# Date: September 2019

from Task_1 import Task1
from Task_2 import Task2


def main():

    print("Week 1 CET323 AI")
    print("1 -> Exercise 1 (Temperature Converter)")
    print("2 -> Exercise 2 (Average any number of numbers)")
    userInput = int(input("Type one of the numbers to run a program: "))

    if userInput == 1:
        task1 = Task1()
        task1.run()
    elif userInput == 2:
        task2 = Task2()
        task2.run()

if __name__ == '__main__':
    main()