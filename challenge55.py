"""
Implement a URL shortener with the following methods:

    shorten(url), which shortens the url into a six-character alphanumeric s
    tring, such as zLg6wl.
    restore(short), which expands the shortened string into the original url.
    If no such shortened string exists, return null.
"""

import hashlib

class UrlShortener:
    
    def __init__(self):
        self.map = dict()
        self.m = hashlib.sha256
        
    def shorten(self, url):
        if url not in self.map.keys():
            encoded = self.m(url.encode()).hexdigest()
            encoded = encoded[:6]
            self.map[encoded] = url
            return encoded
        return None
    
    def restore(self, short):
        return self.map[short]
    
if __name__ == "__main__":
    url_0 = "https://www.tutorialspoint.com/python/string_replace.htm"
    us = UrlShortener()
    short_0 = us.shorten(url_0)
    assert us.restore(short_0) == url_0
    short_1 = us.shorten(url_0)
    assert us.restore(short_1) == url_0