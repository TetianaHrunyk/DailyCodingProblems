"""Gray code is a binary code where each successive value differ in only one bit, 
as well as when wrapping around. Gray code is common in hardware so that
 we don't see temporary spurious values during transitions.

Given a number of bits n, generate a possible gray code for it.

For example, for n = 2, one gray code would be [00, 01, 11, 10]."""

def is_close(a: str, b: str):
    a = bin(a)[2:]
    b = bin(b)[2:]
    if (a.count("1") == (a and b).count("1") - 1) or \
       (a.count("1") == (a and b).count("1") + 1):
        return True
    return False

def generate_grey_code_helper(n: int, curr: list):
    if len(curr) == 2**n:
        if is_close(curr[-1], curr[0]):
            print("[", end = "")
            for c in curr[:-1]:    
#            THIS WILL BREAK IF N > 2            
                print("{:0>2}".format(bin(c)[2:]), end = ", ")
            print("{:0>2}".format(bin(curr[-1])[2:]), end = "]\n")
    for j in range(2**n):
        if is_close(curr[-1], j):
            if j not in curr:
                curr.append(j)
                generate_grey_code_helper(n, curr)
                curr.pop()
    
def generate_grey_code(n: int):
    for i in range(2**n):
        curr = [i]
        generate_grey_code_helper(n, curr)
    
if __name__ == "__main__":
#   IF YOU CHANGE N, PLEASE, CHANGE THE VALUE IN ROWS 23 and 24 AS WELL    
    generate_grey_code(2)
            