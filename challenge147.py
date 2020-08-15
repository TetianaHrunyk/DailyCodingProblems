"""Given a list, sort it using this method:
reverse(lst, i, j), which reverses lst from i to j."""

def reverse(l, i, j):
    l = l[:i] + l[i:j+1][::-1] + l[j+1:]
    return l

def reverse_sort(l: list):
    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            if l[i]>l[j]:
                l = reverse(l, i, j)
    return l
    
    
    

if __name__ == "__main__":
    import random
    random.seed = 1
    l = [random.randint(-5, 5) for _ in range(10)]
    sorted_l = reverse_sort(l)
    assert sorted(l) == sorted_l