"""
Given a string, find the longest palindromic contiguous substring.
 If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". 
The longest palindromic substring of "bananas" is "anana".
"""
def longestPalindrome(s: str) -> str:
    longest = ""
    for i in range(len(s)):
        sub = s[i:]     
        while len(sub) != 1:
            #print("Sub under while loop: ", sub)
            palindrom_found = True
            for j in range(len(sub)//2):
                if sub[j] != sub[-j-1]:
                    palindrom_found = False
                    sub = sub[:-j-1]
                    break
        
            if palindrom_found:
                #print("Palindrom found: ", sub)
                if len(sub) > len(longest):
                    longest = sub
                break
    if not longest:
        #print("Longest from here")
        longest = s[0]
                
    return longest  
    
    
if __name__ == '__main__':
    assert longestPalindrome("aabcdcb") == "bcdcb"
    assert longestPalindrome("bananas") == "anana"
    
    assert longestPalindrome("cbbddd") == "ddd"
    assert longestPalindrome("asdddsa") == "asdddsa"