"""Given a list of integers and a number K, return which contiguous elements of
 the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4],
 since 2 + 3 + 4 = 9.
"""

def cont_elem_sum(l: list, k: int):
    res = []
    for elem in l:
#        print(f"res = {res}, elem = {elem}")
        if elem < k:
            res.append(elem)
            if sum(res) > k:
                res = res[1:]
            if sum(res) == k:
                return res 
        elif elem == k:
            return [k]
        else:
            res = []
    return res if sum(res) == k else []

if __name__ == "__main__":
    assert cont_elem_sum([1, 2, 3, 4, 5], 9) == [2, 3, 4]
    assert cont_elem_sum([1, 2, 3, 4, 5], 1) == [1]
    assert cont_elem_sum([1, 2, 3, 4, 5], 5) == [2, 3]
    assert cont_elem_sum([1, 2, 3, 4, 5, 20], 20) == [20]
    assert cont_elem_sum([1, 2, 3, 4, 5, 20], 35) == [1, 2, 3, 4, 5, 20]