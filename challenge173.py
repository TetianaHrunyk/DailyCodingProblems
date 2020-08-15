"""Write a function to flatten a nested dictionary. Namespace the keys with a period.
For example, given the following dictionary:
{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:
{
    ".key": 3,
    ".foo.a": 5,
    ".foo.bar.baz": 8
}
You can assume keys do not contain dots in them, i.e. no clobbering will occur."""



def flatten(d):
    global flat 
    flat = dict()
    flatten_helper(d)
    return flat
    
def flatten_helper(d: dict, cur_key=""):
    for key, value in d.items():

        
        if type(d[key]) != dict:
            flat[cur_key+"."+key] = value
        else:
            flatten_helper(d[key], cur_key+"."+key)

            
if __name__ == "__main__":
    assert flatten({
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
    }) == {
    ".key": 3,
    ".foo.a": 5,
    ".foo.bar.baz": 8
}


    
    