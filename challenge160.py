"""Given a tree where each edge has a weight, 
compute the length of the longest path in the tree.
    For example, given the following tree:
   a
  /|\
 b c d
    / \
   e   f
  / \
 g   h
and the weights: a-b: 3, a-c: 5, a-d: 8, d-e: 2, d-f: 4, e-g: 1, e-h: 1, 
the longest path would be c -> a -> d -> f, with a length of 17.
    The path does not have to pass through the root, and each node
can have any amount of children."""

class Node:
    
    def __init__(self, val):
        self.val = val
        self.children = {}
        
class WeightedGraph:
    
    def __init__(self):
        self.root = Node('a')
        
    def add_node(self, val, weight, parent):
        
        def add_rec(root, val, weight, parent):
            if root.val == parent:
                new_node = Node(val)
                root.children[new_node] = weight
                return
            else:
                for root_child in root.children.keys():
                    add_rec(root_child, val, weight, parent)
                    
        add_rec(self.root,  val, weight, parent)
        
    def find_longest_path(self):
        #NOTE: even though the task says that the path does not have to pass through root,
        #the paths that do pass through root are always longer than those that do not,
        #so this implementation only considers paths that include root.
        paths = []
        
        def find_longest_path_rec(root, cur_sum):
            if not root.children:
                paths.append(cur_sum)
                return cur_sum
            else:
                for root_child, weight in root.children.items():
                    cur_sum += weight
                    find_longest_path_rec(root_child, cur_sum)
                    cur_sum -= weight
                    
        find_longest_path_rec(self.root, 0)
        return max(paths)
                    
if __name__ == "__main__":
    g = WeightedGraph()            
    g.add_node('b', 3, 'a')
    g.add_node('c', 5, 'a')
    g.add_node('d', 8, 'a')
    g.add_node('e', 2, 'd')
    g.add_node('f', 4, 'd')
    g.add_node('g', 1, 'e')
    g.add_node('h', 1, 'e')
    assert g.find_longest_path() == 12
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        