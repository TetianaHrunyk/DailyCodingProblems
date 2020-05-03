pr'''cons(a, b) constructs a pair, 
and car(pair) and cdr(pair) 
returns the first and last element of that pair. 
For example, car(cons(3, 4)) returns 3,
 and cdr(cons(3, 4)) returns 4.
'''

def cons(a, b):
    return lambda f: f(a, b)

def car(f):
    z = lambda x, y: x
    return f(z)

def cdr(f):
    z = lambda x, y: y
    return f(z)

if __name__ == '__main__':
     assert car(cons(3, 4)) == 3
     assert cdr(cons(3, 4)) == 4