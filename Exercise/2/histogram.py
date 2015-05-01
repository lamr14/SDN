#! /usr/bin/env python2
"""
histogram.py: A program to print "
"""
__author__      = "Seshagiri Prabhu"
__copyright__   = "MIT License"

import random

if __name__=="__main__":
    """
    Main function
    """
    # Generates random numbers
    gen_numbers = []
    for x in xrange(1001):
        gen_numbers.append(int(random.gauss(5, 2)))

    # Finds the frequency of numbers
    normalized = dict((i, gen_numbers.count(i)) for i in gen_numbers)

    # Prints histogram
    for key, value in normalized.iteritems():
        if key > -1 and key < 11:
            print str(key) + ":\t" + (value/10) * "*"
    
