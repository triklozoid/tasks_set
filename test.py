#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string
from datetime import datetime, timedelta

import date_calculation
import lru_cache
import anagram


def test_date_calculation():
    tests_count = 100000
    timedelta_range = 10 ** 8
    for i in xrange(0, tests_count):
        test_date = datetime.now() + timedelta(seconds=random.randint(0, timedelta_range) - timedelta_range / 2)
        result = date_calculation.get_next_draw_date(first_date=test_date)
        td = result - test_date
        assert td.total_seconds() > 0

        scheduled_weekdays = [d['weekday'] for d in date_calculation.draw_schedule]
        assert result.weekday() in scheduled_weekdays
        scheduled_hours = [d['hour'] for d in date_calculation.draw_schedule]
        assert result.hour in scheduled_hours


def test_lru():
    max_size = 4
    @lru_cache.lru(max_size=max_size)
    def sum(a, b):
        return a + b

    for i in xrange(0, 50):
        a = random.randint(1, 2)
        b = random.randint(1, 2)
        assert sum(a, b) == a + b

    cache_info = sum.cache_info()
    assert cache_info[0] == 46
    assert cache_info[1] == max_size
    assert cache_info[2] == max_size
    assert cache_info[3] == max_size


def test_anagram():
    tests_count = 10000
    word_length = 5
    anagrams_count = 20
    words_count = 20
    chars = string.ascii_uppercase + string.ascii_lowercase
    for _ in xrange(0, tests_count):
        def _same_letters(word1, word2):
            result = ''.join(sorted(word1.lower())) == ''.join(sorted(word2.lower()))
            return result

        word = ''.join(random.choice(chars) for _ in xrange(word_length))

        anagrams = [''.join(random.sample(word,len(word))) for _ in xrange(0, anagrams_count)]
        random_words = [''.join(random.choice(chars) for _ in xrange(word_length)) for _ in xrange(0, words_count)]
        random_words = [w for w in random_words if not _same_letters(w, word)]

        result = anagram.find_anagrams(word, anagrams + random_words)
        assert len(result) == len(anagrams), "%s, %s, %s" % (result, anagrams, random_words)
