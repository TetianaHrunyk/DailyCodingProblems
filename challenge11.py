"""Implement an autocomplete system. That is, given a query string s and a set of 
all possible query strings, return all strings in the set that have s as a prefix.
For example, given the query string de and the set of strings [dog, deer, deal], 
return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed 
up queries.
"""
class Node:
    def __init__(self, val, children = []):
        self.val = val
        self.children = children


class Autocomplete:
    
    def __init__(self, word_list):
        self.list = word_list
        self.words = dict()
        for word in word_list: 
            self.add_word(word)
        
    def __repr__(self):
        return str(self.words)
        
    def add_word(self, word):
        
        def add_rec(level, word):
            if not word:
                return
            if word[0] not in level.keys():
                level[word[0]] = dict()
            level = level[word[0]]
            add_rec(level, word[1:])
        
        add_rec(self.words, word)
                    
    def autocomplete(self, prefix):
        options = []
        
        def complete_rec(level, prefix):
            if len(level.keys()) == 0:
                options.append(prefix)
            for key in level.keys():
                prefix += key
                complete_rec(level[key], prefix)
                prefix = prefix[:-1]
        
        level = self.words
        for letter in prefix:
            level = level[letter]
        complete_rec(level, prefix)       
        
        return options
        
       
if __name__ == "__main__":
    auto = Autocomplete(["dog", "deer", "deal", 'cat', 'can', 'camp', 'cost'])
    assert auto.autocomplete('de') == ['deer', 'deal']
    assert auto.autocomplete('do') == ['dog']
    assert auto.autocomplete('ca') == ['cat', 'can', 'camp']