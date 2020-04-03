"""
Given an array of strictly the characters 'R', 'G', and 'B',
 segregate the values of the array so that all the Rs come first, 
 the Gs come second, 
and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'],
 it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""

def segregate(l: list) ->list:
    r, b = 0, -1
    i = 0
    bg = l.count("B") + l.count("G")
#    print("Initial: ", l)
    while r!= (len(l)-bg):
        if l[i] == "R":
            l[i], l[r] = l[r], l[i]
#            print(f"Move R at{i} to {r}")
#            print(f"Step {i}, {l}")          
            r+=1
            i += 1
        elif l[i] == "B":
            l[i], l[b] = l[b], l[i]
#            print(f"Move B at{i} to {b}")
#            print(f"Step {i}, {l}")
            b-=1
            i -= 1
        else:
#            print("Do not move G")
            i += 1
#        print()
        
    return l

if __name__ == "__main__":
    print(segregate(['G', 'B', 'R', 'R', 'B', 'R', 'G']))
    print(segregate(['R', 'R', 'R', 'G', 'G', 'B', 'B']))
    print(segregate(['G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G']))
            