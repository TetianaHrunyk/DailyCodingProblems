"""
Implement an LRU (Least Recently Used) cache. It should be able to be initialized
 with a cache size n, and contain the following methods:

    set(key, value): sets key to value. If there are already n items in 
    the cache and we are adding a new item, then it should also remove the 
    least recently used item.
    get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time."""

class Node:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
    def __str__(self):
        return "(%s, %s)" % (self.key, self.value)

class LRUcache:
    
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("capacity > 0")
        
        self.capacity = capacity
        self.cur_size = 0
        
        self.hash_map = {}
        
        self.head = None
        self.end = None
        
    def set(self, key, value):
        if key in self.hash_map:
            node = self.hash_map[key]
            node.value = value
            
            if self.head != node:
                self.remove(node)
                self.set_head(node)               
        else:
            new_node = Node(key, value)            
            if self.cur_size == self.capacity:
                del self.hash_map[self.end.key]
                self.remove(self.end)
            self.set_head(new_node)
            self.hash_map[key] = new_node
            
    def set_head(self, node):
        if not self.head:
            self.head = node
            self.end = node
        else:
            node.prev = self.head
            self.head.next = node
            self.head = node
        self.cur_size += 1
        
    def remove(self, node):
        if not self.head:
            return
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        
        if not node.next and not node.prev:
            self.head = None
            self.end = None
            
        if self.end = node:
            self.end = node.next
            self.end.prev = None
        self.cur_size -= 1
        
        return node
    
    def get(self, key):
        if key not in self.hash_map:
            return None
        node = self.hash_map[key]
        if self.head == node:
            return node.value
        
        self.remove(node)
        self.set_head(node)
        return node.value
    
    def print_elements(self):
        n = self.head
        print("[head = %s, end = %s]" % (self.head, self.end), end=" ")
        while n:
            print("%s -> " % (n), end = "")
            n = n.prev
        print("NULL")
                
                
                
                
                
                
                
                
                
                