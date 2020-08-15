"""You are given a list of data entries that represent entries 
and exits of groups of people into a building. An entry looks like this:
{"timestamp": 1526579928, count: 3, "type": "enter"}

This means 3 people entered the building. An exit looks like this:
{"timestamp": 1526580382, count: 2, "type": "exit"}
This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most people 
in the building. Return it as a pair of (start, end) timestamps. You can assume 
the building always starts off and ends up empty, i.e. with 0 people inside.
"""

def busiest_time(entries: list):
    inside = 0
    max_inside = 0
    time = [0, 0]
    for i in range(len(entries)):
        e = entries[i]
        if e["type"] == "exit":
            inside -= e["count"]
        else:
            inside += e["count"]
        
        if inside >= max_inside:
            max_inside = inside
            time[0] = e["timestamp"]
            if i != len(entries)-1:
                time[1] = entries[i+1]["timestamp"]
            else:
                time[1] = e["timestamp"]
    return time

if __name__ == '__main__':
    entries = [{"timestamp": 1526579928, "count": 3, "type": "enter"},
               {"timestamp": 1526579929, "count": 1, "type": "enter"},
               {"timestamp": 1526579930, "count": 4, "type": "enter"},
               {"timestamp": 1526579931, "count": 5, "type": "exit"},
               {"timestamp": 1526579932, "count": 1, "type": "enter"}, 
               {"timestamp": 1526579933, "count": 2, "type": "exit"}
            ]
    assert busiest_time(entries) == [1526579930, 1526579931]