#! /usr/bin/env python2
"""
lists.py: A program to play around with lists
"""
__author__      = "Seshagiri Prabhu"
__copyright__   = "MIT License"


if __name__=="__main__":
    """
    Main function
    """

    # Initial list to store 3 values given as per 3(i)
    languages = ['Python', 'C++', 'Java']
    print "Initial List: ", languages

    # New languages to be inserted into the 'languages'
    lang = ['C', 'Perl', 'Ruby', 'R', 'JavaScript', 'Scala', 'PHP']
    print "List to be added: ", lang
    
    # A for loop to insert into new languages into 'languages'
    for x in xrange(len(lang)):
        # Prepend an element
        if x % 2 == 0:
            languages.insert(0, lang[x])
        # Appends an element
        else:
            languages.append(lang[x])
    
    print "List after adding new langauges: "
    # Prints the content in "Index - Language name"
    for x in xrange(len(languages)):
        print ("%d - %s" % (x, languages[x]))

    print "Three middle elementsx10:",
    print languages[(len(languages)/2) - 1]*10 + " " + \
            languages[len(languages)/2]*10 + " " +\
            languages[(len(languages)/2) + 1]*10

    # Store 1 to 1000000 in a list
    number_list = []
    for x in xrange(1, 10001):
        number_list.append(x)
    
    # Store the first 1000 elements of number_list to new list
    comp_number_list = []
    for x in xrange(1000):
        comp_number_list.append(number_list[x])

    # Print the comprehension list in reverse order
    for x in comp_number_list[::-1]:
        print x
    
    # Store the first 10 elements of comp_number_list to new list
    comp_comp_number_list = []
    for x in xrange(10):
        comp_comp_number_list.append(comp_number_list[x])

    # Print the comprehension list in 
    print comp_comp_number_list
