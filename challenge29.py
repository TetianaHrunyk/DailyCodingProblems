"""
Run-length encoding is a fast and simple method of encoding strings. 
The basic idea is to represent repeated successive characters 
as a single count and character. For example, the string
 "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding.
 You can assume the string to be encoded have no digits 
 and consists solely of alphabetic characters.
 You can assume the string to be decoded is valid.
"""

def encode(s: str)->str:
    res = ""
    cur_sym = s[0]
    sym_count = 0
    for char in s:
        if char == cur_sym:
            sym_count += 1
        else:
            res += str(sym_count) + cur_sym
            cur_sym = char
            sym_count = 1
    res += str(sym_count) + cur_sym
    return res

if __name__ == "__main__":
    assert encode("AAAABBBCCDAA") == "4A3B2C1D2A"
            