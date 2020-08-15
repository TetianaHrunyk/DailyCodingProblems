"""Using a read7() method that returns 7 characters from a file, implement readN(n) 
which reads n characters.

For example, given a file with the content “Hello world”, three read7() returns 
“Hello w”, “orld” and then “”.
"""
class ReadChars:
    
    def __init__(self, s):
        self.s = s
    
    def return7(self):
        if len(self.s) == 0:
            return ""
        if len(self.s) <= 7:
            res = self.s
            self.s = ""
            return res
        res = self.s[:7]
        self.s = self.s[7:]
        return res

    def returnN(self, n):
        iterations = n//7
        offset = n%7
        res = ""
        for i in range(iterations):
            res += self.return7()
        res += self.s[:offset]
        self.s = self.s[offset:]
        return res
    
if __name__ == "__main__":
    read = ReadChars("Hello world and everyone around!")
    assert read.return7() == "Hello w"
    assert read.returnN(4) == "orld"