"""Write a map implementation with a get function that lets you retrieve the value
 of a key at a particular time.
It should contain the following methods:
    set(key, value, time): sets key to value for t = time.
    get(key, time): gets the key at t = time.
The map should work like this. If we set a key at a particular time,
 it will maintain that value forever or until it gets set at a later time. 
 In other words, when we get a key at a time, it should return the value 
 that was set for that key set at the most recent time.
Consider the following examples:

d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 2) # set key 1 to value 2 at time 2
d.get(1, 1) # get key 1 at time 1 should be 1
d.get(1, 3) # get key 1 at time 3 should be 2

d.set(1, 1, 5) # set key 1 to value 1 at time 5
d.get(1, 0) # get key 1 at time 0 should be null
d.get(1, 10) # get key 1 at time 10 should be 1

d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 0) # set key 1 to value 2 at time 0
d.get(1, 0) # get key 1 at time 0 should be 2
"""

class Map:
    
    def __init__(self):
        self.obj = dict()
        
    def _set(self, key, val, time):
        if key in self.obj.keys():
            self.obj[key][time] = val
        else:
            self.obj[key] = dict()
            self.obj[key][time] = val
    
    def get(self, key, time):
        if key not in self.obj.keys():
            return None
        if time < min(self.obj[key].keys()):
            return None
        if time in self.obj[key].keys():
            return self.obj[key][time]
        most_recent_time = max(self.obj[key].keys())
        for time_choice, val in self.obj[key].items():
            option = time - time_choice
            if option < most_recent_time:
                if option > 0:
                    most_recent_time = time_choice
        return self.obj[key][most_recent_time]
    
if __name__ == "__main__":
    d = Map()
    d._set(1, 1, 0) # set key 1 to value 1 at time 0
    d._set(1, 2, 2) # set key 1 to value 2 at time 2
    assert d.get(1, 1) == 1 # get key 1 at time 1 should be 1
    assert d.get(1, 3) == 2 # get key 1 at time 3 should be 2
    
    d = Map()
    d._set(1, 1, 5) # set key 1 to value 1 at time 5
    assert d.get(1, 0) == None # get key 1 at time 0 should be null
    assert d.get(1, 10) == 1# get key 1 at time 10 should be 1
    
    d = Map()
    d._set(1, 1, 0) # set key 1 to value 1 at time 0
    d._set(1, 2, 0) # set key 1 to value 2 at time 0
    assert d.get(1, 0) == 2 # get key 1 at time 0 should be 2    
        
        
        
        
        
        
        
        