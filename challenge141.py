"""Implement 3 stacks using a single list:"""

class Stack:
    def __init__(self):
        self.list = []

    def pop(self, stack_number):
        """numbers from 1 to 3"""
        chunks = len(self.list)//3
        for i in range(chunks-1, -1, -1):
            indx = (i+1)*3-(4-stack_number) 
            if self.list[indx] != None:
                res = self.list[indx]
                self.list[indx] = None
                return res
        print()
        return None
        

    def push(self, item, stack_number):
        """numbers from 1 to 3"""
        chunks = len(self.list)//3
        for i in range(chunks):
            indx = (i+1)*3-(4-stack_number) 
            if self.list[indx] == None:
                self.list[indx] = item
                return 
        self.list += [None] * 3
        indx = (chunks+1)*3-(4-stack_number)
        self.list[indx] = item
        
    def __repr__(self):
        return str(self.list)
    
if __name__ == "__main__":
    s= Stack()
    s.push("a", 1)
    s.push("aa", 1)
    
    s.push("b", 2)
    
    s.push("c", 3)
    s.push("cc", 3)
    s.push("ccc", 3)
    
    assert s.pop(1) == "aa"
    assert s.pop(1) == "a"
    
    assert s.pop(2) == "b"
    assert s.pop(2) == None
    
    assert s.pop(3) == "ccc"
        

        
    
        
                