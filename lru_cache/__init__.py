#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter


def lru(max_size=None):
    if max_size is None:
        max_size = 100

    cache = {}
    cache_info = Counter()
    counter = Counter()

    def _cache_info():
        return (
                cache_info['hits'],
                cache_info['misses'],
                max_size,
                len(cache.keys()),
        )

    def _lru(wrapped):
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key not in cache:
                cache_info['misses'] += 1
                if len(cache.keys()) >= max_size:
                    cache.pop(counter.most_common()[:-2:-1][0][0], None)
                    counter.pop(counter.most_common()[:-2:-1][0][0], None)
                cache[key] = wrapped(*args, **kwargs)
            else:
                cache_info['hits'] += 1
            counter[key] += 1
            return cache[key]
        wrapper.cache_info = _cache_info
        return wrapper
    return _lru

