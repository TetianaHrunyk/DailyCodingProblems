"""Find an efficient algorithm to find the smallest distance 
(measured in number of words) between any two given words in a string.
For example, given words "hello", and "world" and a text content of
"dog cat hello cat dog dog hello cat world", return 1 because there's only 
one word "cat" in between the two words."""

def find_distance_in_words(text: str, w1: str, w2: str):
    cur_distance = 0
    min_distance = 0
    w1_found = False
    w2_found = False
    text = text.split(" ")
    for word in text:
        
        if word == w1:
            w1_found = True
            if w2_found:
                if cur_distance < min_distance or min_distance == 0:
                    min_distance = cur_distance
                cur_distance = 0
                w2_found = False
            else:
                cur_distance = 0

        if word == w2:
            w2_found = True
            if w1_found:
                if cur_distance < min_distance or min_distance == 0:
                    min_distance = cur_distance
                cur_distance = 0
                w1_found = False 
            else:
                cur_distance = 0
        
        if w1_found or w2_found:
            cur_distance += 1
            
        #print(f"w1: {w1_found}, w2: {w2_found}, cur_distance: {cur_distance}\n") 
           
    return min_distance-1 if min_distance!=0 else 0

if __name__ == "__main__":
    text = "dog cat hello cat dog dog hello cat world"
    assert find_distance_in_words(text, "hello", "world")  == 1
    assert find_distance_in_words(text, "cat", "cat")  == 0
    assert find_distance_in_words(text, "dog", "world") == 2
    assert find_distance_in_words(text, "dog", "cat") == 0
            