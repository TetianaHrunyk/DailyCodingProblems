"""Given a string and a set of delimiters, reverse the words in the string while 
maintaining the relative order of the delimiters. For example, given "hello/world:here",
 return "here/world:hello"

Follow-up: Does your solution work for the following cases: "hello/world:here/", 
"hello//world:here"
"""

def reverse_word_order(s: str):
    delimeters = []
    words = []
    word = ""
    for char in s:      
        if not char.isalnum():
            if word != "":
                words.append(word)
                delimeters.append("word")
                word = ""
            delimeters.append(char)
        else:
            word += char
    
    if word != "":
        delimeters.append("word")
        words.append(word)
    words = words[::-1]
    
    rvs = ""
    words_count = 0
    for delimiter in delimeters:
        if delimiter == "word":
            rvs += words[words_count]
            words_count += 1
        else:
            rvs += delimiter 
            
    return rvs
    
    
if __name__ == "__main__":
    assert reverse_word_order("here/world:hello") == "hello/world:here"
    assert reverse_word_order("hello/world:here/") == "here/world:hello/"
    assert reverse_word_order("hello//world:here") == "here//world:hello"