"""
Given a dictionary of words and a string made up of those words (no spaces), 
return the original sentence in a list. 
If there is more than one possible reconstruction, 
return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words
 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", 
 you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', 
and the string "bedbathandbeyond", 
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""

def stringToSentence(words: str, string: str):
    sentence = []
    word = ''
    for char in string:
        if word in words:
            sentence.append(word)
            word = char
        else:
            word += char
    if word in words:
        sentence.append(word)
    return sentence if len(sentence) > 0 else None

if __name__ == '__main__':
    
    words = ['quick', 'brown', 'the', 'fox']
    string = "thequickbrownfox"
    assert stringToSentence(words, string) == ['the', 'quick', 'brown', 'fox']
    
    words = ['quick', 'brown', 'the', 'fox']
    string = "thisisjunk"
    assert stringToSentence(words, string) == None
    