# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.

# There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

# Implement the Solution class:

# Solution() Initializes the object of the system.
# String encode(String longUrl) Returns a tiny URL for the given longUrl.
# String decode(String shortUrl) Returns the original long URL for the given shortUrl. It is guaranteed that the given shortUrl was encoded by the same object.

# Use random string and base64 encoding to generate short url
import random
import string


class Codec:
    def __init__(self):
        self.url_map = {}
        self.short_url_map = {}
        self.base_url = 'http://tinyurl.com/'
        self.chars = string.ascii_letters + string.digits

    def encode(self, longUrl: str) -> str:
        if longUrl in self.url_map:
            return self.url_map[longUrl]
        else:
            short_url = self.base_url + ''.join(random.choices(self.chars, k=6))
            self.url_map[longUrl] = short_url
            self.short_url_map[short_url] = longUrl
            return short_url

    def decode(self, shortUrl: str) -> str:
        return self.short_url_map[shortUrl]