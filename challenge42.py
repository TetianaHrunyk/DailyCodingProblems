"""
Given a list of integers S and a target number k, write a function that returns 
a subset of S that adds up to k. If such a subset cannot be made, then return
 null.

Integers can appear more than once in the list. You may assume all numbers 
in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] 
since it sums up to 24.
"""

def prepareData(l: list, s: int) -> list:
    seen = []
    i = 0
    while i < len(l):
        try:
            num = l[i]
            if (num > s) or (num in seen):
                l.remove(num)
            if num == s:
                return num
            else:
                seen.append(num)
                i += 1              
        except:
            break
    
    seen.sort(reverse = True)
    return seen

def subset(l: list, s: int, cur_sub = [], start = 0, end = 1):
    print(f"Start: {start}, end: {end}, cur_sub: {cur_sub}")
    if start >= len(l):
        return None    
    if sum(cur_sub) == s:
        return cur_sub
    elif sum(cur_sub) > s:
#        print("Cur_sum is greater than s")
        if end >= len(l):
            start += 1
            end = start + 1
            cur_sub = [l[start]]           
            return subset(l, s, cur_sub, start, end)
        else:
            cur_sub.pop()
            end+=1
            return subset(l, s, cur_sub, start, end)
    else:
#        print("Cur_sum is less than s")
        if end >= len(l):
            start += 1
            end = start + 1
            cur_sub = [l[start]]           
            return subset(l, s, cur_sub, start, end)
        else:
            cur_sub.append(l[end])
            end += 1
            return subset(l, s, cur_sub, start, end)
        
                
        










if __name__ == "__main__":
    print(subset(prepareData([12, 1, 61, 5, 5, 9, 2], 24), 24))