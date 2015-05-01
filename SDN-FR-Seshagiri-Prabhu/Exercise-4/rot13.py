#! /usr/bin/env python2
"""
rot13.py: Ceaser cipher
"""
__author__      = "Seshagiri Prabhu"
__copyright__   = "MIT License"


key_map = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
         'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
         'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
         'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
         'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
         'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
         'W':'J', 'X':'K', 'Y':'L', 'Z':'M', ' ': ' '}


class Ceaser:
    """
    This is the main parent class of Ceaser cipher
    """
    def __init__(self, input_string):
        self.string = input_string


    def encode(self):
        """
        A function to encode string
        """
        out_string = ''
        for x in self.string:
            out_string += key_map[x]
        return out_string 
   

    def decode(self):
        """
        A function to decode string
        """
        out_string = ''
        for x in self.string:
            for key,value in key_map.iteritems():
                if x == value:
                    out_string += key
        return out_string


if __name__=="__main__":
    """
    Main function
    """
    input_string_encode = raw_input("Enter the string you want to encode: ")
    encode = Ceaser(input_string_encode)
    print "Encoded string: " + encode.encode()

    input_string_decode = raw_input("Enter the string you want to decode: ")
    decode = Ceaser(input_string_decode)
    print "Decoded string: " + decode.decode()
