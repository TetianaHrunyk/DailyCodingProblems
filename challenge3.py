"""
Given the root to a binary tree, implement serialize(root), 
which serializes the tree into a string, and deserialize(s), 
which deserializes the string back into the tree.
"""
import json


class Node:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

def serialize(root):
    def _serialize(root):
        serialize_arr = []
        if root.value:
            serialize_arr.append(root.value)
        if root.left:
            serialize_arr.append(_serialize(root.left))
        else:
            serialize_arr.append(None)
        if root.right:
            serialize_arr.append(_serialize(root.right))
        else:
            serialize_arr.append(None)
        return serialize_arr
    return json.dumps(_serialize(root))

def deserialize(string):
    if string == None:
        return None
    node_list = json.loads(string) if type(string) == str else string
    root = Node(node_list[0], deserialize(
        node_list[1]), deserialize(node_list[2]))
    return root

if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    
    assert deserialize(serialize(node)).left.left.value == 'left.left'