"""Given a string of words delimited by spaces, reverse the words in string. 
For example, given "hello world here", return "here world hello"

Follow-up: given a mutable string representation, can you perform this operation 
in-place?
"""

def reverse_word_order(phrase: str):
    words = phrase.split(" ")
    words = words[::-1]
    return " ".join(words)

def follow_up(phrase: str):
    in_index = 0
    word_len = 0
    phrase+= " "
    for i in range(len(phrase)):
        if phrase[-1] == " ":
            in_index += word_len
            word_len = 0
        phrase =  phrase[:in_index] + phrase[-1] + phrase[in_index:-1]
        word_len += 1
    return phrase[:-1]
            
    
    
if __name__ == "__main__":
    assert reverse_word_order("hello world here") == "here world hello"
    assert follow_up("hello world here") == "here world hello"
    