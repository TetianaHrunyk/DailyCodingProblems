"""Given a mapping of digits to letters (as in a phone number), and a digit string, 
return all possible letters the number could represent. You can assume each valid number
 in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], "3": [“d”, “e”, “f”], …} 
then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
"""

def CartesianProduct(left, right):
    res = []
    for l in left:
        for r in right:
            if (l+r) not in res:
                res.append(l+r)
    return res

def mapDigitsToStrings(digit: str, digit_map: dict):
    res = CartesianProduct(digit_map[digit[0]], digit_map[digit[1]])
    for d in range(2, len(digit)):
        right = digit_map[digit[d]]
        local_res = CartesianProduct(res, right)
        res += local_res
    return res

if __name__ == "__main__":
    assert mapDigitsToStrings("23", {"2": ["a", "b", "c"], "3": ["d", "e", "f"]}) == \
            ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    
    assert mapDigitsToStrings("235", {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "5": ["z", "x", "c"]})\
    == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf', 'adz', 
        'adx', 'adc', 'aez', 'aex', 'aec', 'afz', 'afx', 'afc', 'bdz', 'bdx', 
        'bdc', 'bez', 'bex', 'bec', 'bfz', 'bfx', 
        'bfc', 'cdz', 'cdx', 'cdc', 'cez', 'cex', 'cec', 'cfz', 'cfx', 'cfc']
    
    assert mapDigitsToStrings("23", {"2": [], "3": []}) == []