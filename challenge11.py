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
    
    def __init__(self):
        self.options = Node("")
        
    def add_node(self, root, parent, node, k = 1):
        if root.val in node.val and k<50:
            print(f"parent {parent.val}, root {root.val}, k = {k}")
            parent = root
            k+=1
            for child in root.children:
                self.add_node(child, parent, node, k)
            parent.children.append(node)
        
    def construct(self, options):
        options.sort()
        for option in options:
            for i in range(len(option)):
                new_node = Node(option[:i], [])
                self.add_node(self.options, self.options, new_node)
        
if __name__ == "__main__":
    auto = Autocomplete()
    auto.construct(["dog", "deer", "deal"])