# File: Task_2.py
# Description: Task_2 class file
# Author: F. Eduard Decu
# Date: September 2019

class Task2():
    def __init__(self):
        pass

    def run(self):
        print("###############Exercise 2 ################")
        number = int(input("How many numbers: "))
        total = 0

        for x in range(number):
            n = float(input('Type a number: '))
            total += n

        average = total / number
        print('The average of {0} numbers is : {1}'.format(number, average))