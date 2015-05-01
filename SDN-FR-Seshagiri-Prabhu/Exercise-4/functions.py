#! /usr/bin/env python2
"""
functions.py: A program to try out the python functions
"""
__author__      = "Seshagiri Prabhu"
__copyright__   = "MIT License"


def division_by_zero():
    """
    A function to test try-catch during 
    a division_by_zero
    """
    try:
        x = 10/0
    except ZeroDivisionError:
        print "Oops! Division by zero found"


def odd_or_even():
    """
    A function which takes integer input and
    computes whether its odd or even
    """
    input = int(raw_input("Enter the integer: "))
    if input%2 == 0:
        print "Given integer is even"
    elif input%2 == 1:
        print "Given integer is odd"
    else:
        print "Given input is not an integer"


def two_string_input_output_concatinate():
    """
    A function which takes two string inputs
    gives a concatinated output string
    """
    string1 = raw_input("Enter the first string: ")
    string2 = raw_input("Enter the second string: ")
    print string1 + string2


if __name__=="__main__":
    """
    Main function
    """
    two_string_input_output_concatinate()
    odd_or_even()
    division_by_zero()
