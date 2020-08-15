"""Design and implement a HitCounter class that keeps track of requests (or hits). 
It should support the following operations:
    record(timestamp): records a hit that happened at timestamp
    total(): returns the total number of hits recorded
    range(lower, upper): returns the number of hits that occurred between timestamps 
    lower and upper (inclusive)
Follow-up: What if our system has limited memory?
"""
import datetime
import pandas as pd

class HitCounter:
    
    def __init__(self):
        self.hit_times = []
        
    def record(self, timestamp = None):
        """Takes timestamp as a list of values
        and converts them to a python timestamp"""
        if timestamp == None:
            timestamp = datetime.datetime.now()
        else:
            timestamp = datetime.datetime(*timestamp)
        self.hit_times.append(pd.to_datetime(timestamp))
        
    def total(self):
        return len(self.hit_times)
    
    def trange(self, lower, upper):
        lower = pd.to_datetime(datetime.datetime(*lower))
        upper = pd.to_datetime(datetime.datetime(*upper))
        count = 0
        for hit_time in self.hit_times:
            if hit_time >= lower and hit_time <= upper:
                count += 1
        return count
    
if __name__ == "__main__":
    hits = HitCounter()
    hits.record((2020, 6, 19))
    hits.record((2020, 6, 20))
    hits.record((2020, 6, 21))
    hits.record((2020, 6, 16))
    hits.record((2020, 6, 17))
    hits.record((2020, 6, 18))

    assert hits.total() == 6
    assert hits.trange((2020, 6, 18), (2020, 6, 21)) == 4