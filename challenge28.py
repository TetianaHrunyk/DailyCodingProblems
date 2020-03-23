"""
Write an algorithm to justify text. Given a sequence of words and an integer
 line length k, return a list of strings which represents each line, 
 fully justified.

More specifically, you should have as many words as possible in each line.
 There should be at least one space between each word. Pad extra spaces
 when necessary so that each line has exactly length k. 
 Spaces should be distributed as equally as possible, with the extra spaces,
 if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad 
the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words
 ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] 
 and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""

def distribute(words: list, k: int) ->list:
    lines = []
    line = ""
    for word in words:
        if len(line) + (len(word)) == k:
            line += word
            lines.append(line)
            line = ""
        elif len(line) + (len(word)) < k:
            word_with_space = word + ' '
            line += word_with_space
        else:
            lines.append(line)
            line = word + ' '
    if line:
        lines.append(line)
        
    evenly_distributed_lines = []
    new_line = ""
    for line in lines:
        if line[-1] == ' ':
            line = line[:-1]
        spaces_to_add = k - len(line)
        if spaces_to_add == 0:
            continue
        else:
            spaces_in_line = line.count(' ')
            spaces_to_distribute = spaces_to_add // spaces_in_line 
            extra_spaces = spaces_to_add % spaces_in_line 
            for char in line:
                if char != ' ':
                    new_line += char
                else:
                    new_line += ' ' + ' '*spaces_to_distribute
                    if extra_spaces != 0:
                        new_line += ' '*extra_spaces
                        extra_spaces = 0
            evenly_distributed_lines.append(new_line)
            new_line = ""
    
    return evenly_distributed_lines

def print_lines(lines: list):
    for line in lines:
        print(line)

if __name__ == "__main__":
    words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    k = 16
    print_lines(distribute(words, k))