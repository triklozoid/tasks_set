#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

def find_anagrams(word, words_list):
    result = []
    word_counter = Counter(word.lower())
    for lword in words_list:
        if word_counter == Counter(lword.lower()):
            result.append(lword)
    return result
