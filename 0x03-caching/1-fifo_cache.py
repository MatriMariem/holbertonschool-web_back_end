#!/usr/bin/python3
""" FIFOCache """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache Class """

    def __init__(self):
        """ constructor """
        super().__init__()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data
        the item value for the key key
        """
        abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    for i in abc:
                        if i in self.cache_data:
                            break
                    del self.cache_data[i]
                    print("DISCARD:", i)
                self.cache_data[key] = item

    def get(self, key):
        """
        return the value of key in self.cache_data
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
