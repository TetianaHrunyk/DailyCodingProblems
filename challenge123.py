"""Given a string, return whether it represents a number. 
Here are the different kinds of numbers:
    "10", a positive integer
    "-10", a negative integer
    "10.1", a positive real number
    "-10.1", a negative real number
    "1e5", a number in scientific notation
And here are examples of non-numbers:
    "a"
    "x 1"
    "a -2"
    "-"     """
    
import re

def is_number(s):
    number = re.match("^-?[0-9]+[.e]?[0-9]+$", s)  
    return True if number else False

if __name__ == "__main__":
    assert is_number("10") == True
    assert is_number("-10") == True
    assert is_number("-10.1") == True
    assert is_number("10.1") == True
    assert is_number("1e5") == True
    
    assert is_number("1e.5") == False
    assert is_number("a") == False
    assert is_number("x 1") == False
    assert is_number("a -2") == False
    assert is_number("-") == False