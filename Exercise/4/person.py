#! /usr/bin/env python2
"""
person.py: A program to create a parent class and two 
child classes of the same
"""
__author__      = "Seshagiri Prabhu"
__copyright__   = "MIT License"


class Person():
    """
    This is the main parent class for a person
    """
    gender = "Null"
    def get_gender(self):
        return gender


class Male(Person):
    """
    This is a child class of person belongs to all males
    """
    gender = "Male"
    def get_gender(self):
        return gender


class Female(Person):
    """
    This is a child class of person belongs to all females
    """
    gender = "Female"
    def get_gender(self):
        return gender


if __name__=="__main__":
    """
    Main function
    """

