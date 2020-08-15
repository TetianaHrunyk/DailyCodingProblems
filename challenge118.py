"""Given a sorted list of integers, square the elements and give the output
 in sorted order.
For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
"""
def square_and_sort_one_line(l: list):
    return sorted([i**2 for i in l])

def merge(a, b, res = []):
    if a and b:
        if a[0] <= b[0]:
            res.append(a[0])
            merge(a[1:], b, res)
        else:
            res.append(b[0])
            merge(a, b[1:], res)
    else:
        if a:
            res += a
        if b:
            res += b
    return res

def square_and_sort(l: list):
    neg_sq = [i**2 for i in l if i < 0][::-1]
    pos_sq = [i**2 for i in l if i >= 0]
    return merge(neg_sq, pos_sq)

if __name__ == "__main__":
    assert square_and_sort([-9, -2, 0, 2, 3]) == [0, 4, 4, 9, 81]

            
            