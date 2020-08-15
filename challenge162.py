"""Given a list of words, return the shortest unique prefix of each word. 
For example, given the list:
    dog
    cat
    apple
    apricot
    fish
Return the list:
    d
    c
    app
    apr
    f
"""

class WordsTree:
    
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
                    
    def get_sups(self):
        
        def get_sup_rec(level, word):
            sup = word[0]
            for letter in word[1:]:
                sup += letter
                if len(level.keys()) > 1:
                    return sup
                level = level[letter]
            return word[0]
                    
        return [get_sup_rec(self.words[word[0]], word) for word in self.list]
        
            
    
    
            
if __name__ == "__main__":
    words = WordsTree(['dog', 'cat', 'apple', 'apricot', 'fish'])
    assert words.get_sups() == ['d', 'c', 'app', 'apr', 'f']
    
    