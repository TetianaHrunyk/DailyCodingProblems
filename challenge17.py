class Node:
    def __init__(self, val, depth, parent = None, children = []):
        self.val = val
        self.depth = depth
        self.parent = parent
        self.children = children
        
class FileSystem:
    
    def __init__(self):
        self.root = None
    
    def build_system(self, structure):
        s = structure.split("\n")
        self.root = Node(s[0], 0)
        tail = self.root
        for elem in s[1:]:
            depth = elem.count("\t")
            elem = elem.strip("\t")
            
            if depth > tail.depth:
                new_elem = Node(elem, depth, tail, [])
                tail.children.append(new_elem)
                
            elif depth == tail.depth:
                new_elem = Node(elem, depth, tail.parent, [])
                tail.parent.children.append(new_elem)

            else:
                while tail.depth > depth:
                    tail = tail.parent
                new_elem = Node(elem, depth, tail.parent, [])
                tail.parent.children.append(new_elem)
            
     
        
if __name__ == "__main__":
    s = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    fsys = FileSystem()
    fsys.build_system(s)

    
    
    
    
    
    
    
    
    
    
                 
                
        
        