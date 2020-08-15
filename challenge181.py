"""Given a string, split it into as few strings as possible such that each string 
is a palindrome.
For example, given the input string racecarannakayak, return 
["racecar", "anna", "kayak"].
Given the input string abc, return ["a", "b", "c"]."""

def is_palindrome(a):
    return a == a[::-1]

def fpalindromes(s, palindromes):
    print(f"s = {s}, pals = {palindromes}")
    if s == '':
        p.append( palindromes)
    for i in range(len(s)):
        if is_palindrome(s[:i]):
            palindromes.append(s[:i])
            fpalindromes(s[i+1:], palindromes)
            palindromes.pop()
        
def smallest_palindromes_num(s):
    p = []
    fpalindromes(s, [])
    print(p)
    p = sorted(p, key = lambda x: len(x))
    return p[0]
    


if __name__ == "__main__":
    print(smallest_palindromes_num('racecarannakayak'))
        