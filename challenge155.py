"""Given a list of elements, find the majority element, which appears more than
 half the time (> floor(len(lst) / 2.0)).
You can assume that such element exists.
For example, given [1, 2, 1, 1, 3, 4, 0, 1], return 1."""
import math

def find_majority_elem(l: list):
    length = len(l)
    margin = math.floor(length/ 2.0)
    l = sorted(l)
    counter = 0
    while True:
        #even though we assume that the return value exists, it is better
        #to make sure that the loop will not be infinite
        if counter == length-1:
            break
        if l.count(l[counter]) > margin:
            return l[counter]
        
        else:
            while l[counter] == l[counter+1]:
                counter += 1
            counter +=1
            
    
if __name__ == "__main__":
    assert find_majority_elem([1, 2, 1, 1, 3, 4, 0, 1, 1]) == 1
            
        