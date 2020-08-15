"""Given two rectangles on a 2D graph, return the area of their intersection. 
If the rectangles don't intersect, return 0.
For example, given the following rectangles:
{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}
and
{
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}
return 6."""

def get_area(r1, r2):
    width_r1 = {i for i in range(r1["top_left"][0], r1["top_left"][0] + r1["dimensions"][0])}
    height_r1 = {i for i in range(r1["top_left"][1], r1["top_left"][1] + r1["dimensions"][1])}
    
    width_r2 = {i for i in range(r2["top_left"][0], r2["top_left"][0] + r2["dimensions"][0])}
    height_r2 = {i for i in range(r2["top_left"][1], r2["top_left"][1] + r2["dimensions"][1])}

    return len(width_r1 & width_r2)*len(height_r2 & height_r1)

if __name__ == "__main__":
    r1 = {
        "top_left": (1, 4),
        "dimensions": (3, 3) # width, height
    }
    
    r2 = {
        "top_left": (0, 5),
        "dimensions": (4, 3) # width, height
    }
    
    assert get_area(r1, r2) == 6