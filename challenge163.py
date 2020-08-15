"""The expression is given as a list of numbers and operands. For example:
[5, 3, '+'] should return 5 + 3 = 8.

For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] 
should return 5, since it is equivalent to 
((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.
You can assume the given expression is always valid."""

def eval_rev_polish_not(q):
    infix = ''
    for elem in q:
        if type(elem) == int:
            infix += '('+str(elem)+'_'
        else:
            if infix[-1] == "_":
                infix = infix[:-1]
            for i in range(len(infix)-1, -1, -1):
                if infix[i] == "_":
                    infix = infix[:i]+elem+infix[i+1:]
                    break
            infix += ")"
            infix += "_"
    infix = infix[:-1]+')'
            
    return eval(infix)

if __name__ == "__main__":
    assert eval_rev_polish_not(\
            [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']) == 5