#!/usr/bin/env python3
"""
FIFO caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    a class that inherits from
    BaseCaching and is a caching system
    """
    def __init__(self):
        """
        initializes the cache
        """
        super().__init__()
        self.cache_data = {}
    
    def put(self, key, item):
        """

        """
        if key and item:
            self.cache_data[key] = item

        else:
            pass