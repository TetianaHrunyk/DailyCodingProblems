def number_k(num: list, k: int) -> bool:
    assert type(num) == list
    assert type(k) == int
    
    if sum(num) < k:
        return False
    else:
        length = len(num)
        for i in range(length):
            for j in range(i + 1, length):
                if (num[i] + num[j]) == k:
                    return True               
        return False